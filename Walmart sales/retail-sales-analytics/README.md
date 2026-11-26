# Retail Sales Analytics — Walmart Dataset

An end-to-end, reproducible retail sales analytics case study using **Python, MySQL, and Power BI**. This project starts from the Walmart sales CSV already stored in this repository and creates a repeatable analysis workflow with summary tables, data-quality checks, charts, SQL analysis, and a Power BI dashboard build guide.

## Source files

- [Original CSV dataset](../WalmartSalesData.csv.csv)
- [MySQL 8 database dump](../walmartsales_backup.sql)
- [20 reusable SQL analysis queries](../analysis_queries.sql)

## Project structure

```text
Walmart sales/
├── WalmartSalesData.csv.csv       # source dataset (already in this repository)
├── walmartsales_backup.sql        # MySQL database dump
├── analysis_queries.sql           # reusable MySQL analysis queries
└── retail-sales-analytics/
    ├── README.md
    ├── analyze_sales.py           # Python analysis pipeline
    ├── requirements.txt
    ├── powerbi_guide.md           # data model, DAX, report pages
    ├── data_dictionary.md
    └── .gitignore
```

## Dataset snapshot

The source CSV was inspected when this project was prepared. It contains **1,000 transaction rows and 17 source columns**, with dates from **1 January 2019 through 30 March 2019**. The checked dataset totals are:

| Metric | Value |
|---|---:|
| Transactions / unique invoice IDs | 1,000 |
| Units sold | 5,510 |
| Total sales | 322,966.75 |
| Cost of goods sold | 307,587.38 |
| Gross income | 15,379.37 |
| Average invoice value | 322.97 |
| Average customer rating | 6.97 / 10 |
| Gross income as % of sales | 4.76% |

Values are in the dataset's recorded currency units; the source file does not establish a currency symbol in its fields. These are descriptive results for this dataset and period, not forecasts or claims about current Walmart performance.

### A few descriptive findings

- January has the highest total sales among the three months (116,291.87).
- Food and beverages is the highest-sales product line (56,144.84).
- Naypyitaw is the highest-sales city (110,568.71).
- Cash is the highest-sales payment method (112,206.57).
- Saturday has the highest sales among weekdays (56,120.81).

The Python script recomputes these values from the source file, so results should be refreshed after the data changes.

## 1. Run the Python analysis

Requirements: Python 3.10 or later is recommended.

Open a terminal in this folder:

```bash
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Install packages and run the workflow:

```bash
python -m pip install -r requirements.txt
python analyze_sales.py
```

The script expects the original CSV one directory above this folder. To use a different file or output location:

```bash
python analyze_sales.py --input "/path/to/WalmartSalesData.csv.csv" --output-dir "./outputs"
```

### Generated outputs

The script creates the following files under `outputs/`:

- `summary.json` — core KPIs and data-quality checks.
- `data_quality_report.csv` — missing values, duplicate invoice IDs, parsing checks, and date coverage.
- `sales_by_product_line.csv`
- `sales_by_branch_city.csv`
- `sales_by_payment_method.csv`
- `sales_by_customer_type.csv`
- `sales_by_gender.csv`
- `sales_by_month.csv`
- `sales_by_weekday.csv`
- `sales_by_hour.csv`
- `monthly_sales.png`, `product_line_sales.png`, `city_sales.png`

Generated outputs are excluded from Git by the included `.gitignore`; run the script locally to reproduce them.

## 2. Run the MySQL analysis

The parent folder contains the MySQL 8 dump and a companion SQL file with 20 analysis examples.

From the parent `Walmart sales/` folder, load the dump:

```bash
mysql -u root -p < "walmartsales_backup.sql"
```

Then run:

```bash
mysql -u root -p walmartsales < "analysis_queries.sql"
```

The SQL examples cover KPIs, product lines, branches/cities, payment methods, customers, ratings, time trends, rankings, CTEs, and window functions. MySQL 8.0 or later is recommended.

## 3. Build the Power BI dashboard

Follow [powerbi_guide.md](powerbi_guide.md) for CSV import, date modeling, DAX measures, suggested pages, and validation checks. Power BI Desktop is needed to create and interact with the PBIX report. The guide provides the implementation specification; it is not itself a PBIX file.

## 4. Analysis workflow

```text
Walmart CSV
   ├── Python: validation, KPIs, grouped summaries, charts
   ├── MySQL: reproducible SQL analysis and window functions
   └── Power BI: date model, DAX measures, interactive report
                         ↓
                Business interpretation
```

## Reproducibility and limitations

- Keep the source CSV unchanged; use a separate copy for experiments.
- Check the data-quality report before interpreting any metric.
- Confirm the currency/unit from the original dataset publisher before displaying a currency symbol.
- The dataset covers only a three-month historical sample. Avoid describing it as current Walmart operating data.
- Correlation or descriptive differences do not by themselves prove causation.
- Power BI visuals and DAX should be validated in Power BI Desktop after import.

## Author

**Sruthi Laya Perla**
