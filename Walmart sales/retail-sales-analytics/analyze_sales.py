"""Reproducible Walmart sales analysis.

Run from this directory:
    python -m pip install -r requirements.txt
    python analyze_sales.py

The source CSV is expected one directory above this project folder.
Outputs are written to ./outputs/.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = PROJECT_DIR.parent / "WalmartSalesData.csv.csv"
DEFAULT_OUTPUT = PROJECT_DIR / "outputs"

REQUIRED_COLUMNS = [
    "Invoice ID", "Branch", "City", "Customer type", "Gender",
    "Product line", "Unit price", "Quantity", "Tax 5%", "Total",
    "Date", "Time", "Payment", "cogs", "gross margin percentage",
    "gross income", "Rating",
]
NUMERIC_COLUMNS = [
    "Unit price", "Quantity", "Tax 5%", "Total", "cogs",
    "gross margin percentage", "gross income", "Rating",
]


def load_data(csv_path: Path) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Load the dataset, validate its schema, and derive analysis fields."""
    if not csv_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {csv_path}\n"
            "Pass the CSV path with --input or place it beside this project folder."
        )

    df = pd.read_csv(csv_path)
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {missing_columns}")

    raw_rows = len(df)
    missing_cells_before = int(df[REQUIRED_COLUMNS].isna().sum().sum())
    duplicate_invoice_rows = int(df["Invoice ID"].duplicated().sum())

    for column in NUMERIC_COLUMNS:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    invalid_dates = int(df["Date"].isna().sum())
    if invalid_dates:
        raise ValueError(f"{invalid_dates} rows contain invalid dates. Review the source CSV.")

    df["Time Parsed"] = pd.to_datetime(
        df["Time"].astype(str), format="%H:%M:%S", errors="coerce"
    )
    df["Year-Month"] = df["Date"].dt.to_period("M").astype(str)
    df["Day Name"] = df["Date"].dt.day_name()
    df["Day Number"] = df["Date"].dt.dayofweek
    df["Hour"] = df["Time Parsed"].dt.hour

    quality = {
        "source_file": csv_path.name,
        "row_count": raw_rows,
        "column_count": len(df.columns) - 4,
        "unique_invoice_ids": int(df["Invoice ID"].nunique()),
        "duplicate_invoice_rows": duplicate_invoice_rows,
        "missing_cells_in_source_columns": missing_cells_before,
        "invalid_dates": invalid_dates,
        "unparseable_times": int(df["Time Parsed"].isna().sum()),
        "numeric_nulls_after_conversion": int(df[NUMERIC_COLUMNS].isna().sum().sum()),
        "start_date": df["Date"].min().date().isoformat(),
        "end_date": df["Date"].max().date().isoformat(),
    }
    return df, quality


def grouped_sales(
    df: pd.DataFrame,
    by: str | list[str],
    sort_by: str = "Sales",
) -> pd.DataFrame:
    result = (
        df.groupby(by, dropna=False)
        .agg(
            Invoices=("Invoice ID", "nunique"),
            Units_Sold=("Quantity", "sum"),
            Sales=("Total", "sum"),
            Gross_Income=("gross income", "sum"),
            Average_Rating=("Rating", "mean"),
        )
        .reset_index()
    )
    return result.sort_values(sort_by, ascending=False)


def save_bar_chart(
    data: pd.DataFrame,
    category: str,
    value: str,
    title: str,
    output_path: Path,
    horizontal: bool = False,
) -> None:
    plot_data = data.sort_values(value, ascending=horizontal)
    fig, ax = plt.subplots(figsize=(10, 5.5))
    if horizontal:
        ax.barh(plot_data[category].astype(str), plot_data[value])
        ax.set_xlabel(value.replace("_", " "))
    else:
        ax.bar(plot_data[category].astype(str), plot_data[value])
        ax.set_ylabel(value.replace("_", " "))
        ax.tick_params(axis="x", rotation=25)
    ax.set_title(title)
    ax.grid(axis="x" if horizontal else "y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(output_path, dpi=160)
    plt.close(fig)


def run_analysis(input_path: Path, output_dir: Path) -> dict[str, Any]:
    df, quality = load_data(input_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    total_sales = float(df["Total"].sum())
    gross_income = float(df["gross income"].sum())
    cogs = float(df["cogs"].sum())
    invoice_count = int(df["Invoice ID"].nunique())

    summary = {
        **quality,
        "total_sales": round(total_sales, 2),
        "units_sold": int(df["Quantity"].sum()),
        "cost_of_goods_sold": round(cogs, 2),
        "gross_income": round(gross_income, 2),
        "average_invoice_value": round(total_sales / invoice_count, 2) if invoice_count else 0,
        "average_rating": round(float(df["Rating"].mean()), 2),
        "gross_income_margin_pct": round(
            gross_income / total_sales * 100, 2
        ) if total_sales else 0,
    }

    product = grouped_sales(df, "Product line")
    city = grouped_sales(df, ["Branch", "City"])
    payment = grouped_sales(df, "Payment")
    customer = grouped_sales(df, "Customer type")
    gender = grouped_sales(df, "Gender")
    monthly = grouped_sales(df, "Year-Month").sort_values("Year-Month")
    weekday = (
        grouped_sales(df, ["Day Number", "Day Name"])
        .sort_values("Day Number")
        .drop(columns=["Day Number"])
    )
    hourly = (
        df.dropna(subset=["Hour"])
        .groupby("Hour")
        .agg(Invoices=("Invoice ID", "nunique"), Sales=("Total", "sum"))
        .reset_index()
        .sort_values("Hour")
    )

    tables = {
        "sales_by_product_line.csv": product,
        "sales_by_branch_city.csv": city,
        "sales_by_payment_method.csv": payment,
        "sales_by_customer_type.csv": customer,
        "sales_by_gender.csv": gender,
        "sales_by_month.csv": monthly,
        "sales_by_weekday.csv": weekday,
        "sales_by_hour.csv": hourly,
    }
    for filename, table in tables.items():
        table.to_csv(output_dir / filename, index=False, float_format="%.2f")

    quality_rows = [
        {"metric": key, "value": value}
        for key, value in quality.items()
    ]
    pd.DataFrame(quality_rows).to_csv(output_dir / "data_quality_report.csv", index=False)
    (output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    save_bar_chart(
        monthly, "Year-Month", "Sales", "Monthly Sales",
        output_dir / "monthly_sales.png"
    )
    save_bar_chart(
        product, "Product line", "Sales", "Sales by Product Line",
        output_dir / "product_line_sales.png", horizontal=True
    )
    save_bar_chart(
        city, "City", "Sales", "Sales by City",
        output_dir / "city_sales.png"
    )

    print("\nWalmart Sales Analysis")
    print("=" * 25)
    for key in (
        "row_count", "unique_invoice_ids", "total_sales", "units_sold",
        "cost_of_goods_sold", "gross_income", "average_invoice_value",
        "average_rating", "gross_income_margin_pct", "start_date", "end_date",
    ):
        print(f"{key.replace('_', ' ').title():28}: {summary[key]}")
    print(f"\nOutputs saved to: {output_dir}")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze the Walmart sales CSV.")
    parser.add_argument(
        "--input", type=Path, default=DEFAULT_INPUT,
        help="Path to WalmartSalesData.csv.csv"
    )
    parser.add_argument(
        "--output-dir", type=Path, default=DEFAULT_OUTPUT,
        help="Directory for generated CSV, JSON, and chart outputs"
    )
    args = parser.parse_args()
    run_analysis(args.input.expanduser().resolve(), args.output_dir.expanduser().resolve())


if __name__ == "__main__":
    main()
