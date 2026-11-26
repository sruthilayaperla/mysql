# Power BI Dashboard Build Guide

This guide describes how to build the Power BI report for the Walmart sales case study. It is an implementation guide, not a prebuilt PBIX file.

## 1. Import the data

1. Open Power BI Desktop.
2. Select **Get data → Text/CSV**.
3. Select `WalmartSalesData.csv.csv` in the parent `Walmart sales/` folder.
4. Confirm that the delimiter is comma and that the first row is used as headers.
5. In Power Query, set the data types:
   - `Invoice ID`, `Branch`, `City`, `Customer type`, `Gender`, `Product line`, and `Payment`: Text
   - `Unit price`, `Tax 5%`, `Total`, `cogs`, `gross margin percentage`, `gross income`, and `Rating`: Decimal number
   - `Quantity`: Whole number
   - `Date`: Date
   - `Time`: Time
6. Rename the query/table to `Sales`, then select **Close & Apply**.

## 2. Create a calendar table

Create this calculated table in Modeling → New table:

```dax
Calendar =
CALENDAR (
    MIN ( Sales[Date] ),
    MAX ( Sales[Date] )
)
```

Add a calculated year-month column:

```dax
Year Month = FORMAT ( Calendar[Date], "YYYY-MM" )
```

Add a month sort key:

```dax
Year Month Sort = YEAR ( Calendar[Date] ) * 100 + MONTH ( Calendar[Date] )
```

Select `Calendar[Year Month]` and choose **Sort by column → Year Month Sort**. Mark Calendar as the date table using `Calendar[Date]`.

Create a one-to-many relationship from `Calendar[Date]` to `Sales[Date]` (Calendar on the one side). Confirm that both columns have the Date data type.

## 3. Create core DAX measures

Create these measures in the Sales table or a dedicated Measures table:

```dax
Total Sales =
SUM ( Sales[Total] )

Total Orders =
DISTINCTCOUNT ( Sales[Invoice ID] )

Units Sold =
SUM ( Sales[Quantity] )

Cost of Goods Sold =
SUM ( Sales[cogs] )

Gross Income =
SUM ( Sales[gross income] )

Average Order Value =
DIVIDE ( [Total Sales], [Total Orders] )

Average Rating =
AVERAGE ( Sales[Rating] )

Gross Income Margin % =
DIVIDE ( [Gross Income], [Total Sales] )

Tax Amount =
SUM ( Sales[Tax 5%] )

Previous Month Sales =
CALCULATE (
    [Total Sales],
    DATEADD ( Calendar[Date], -1, MONTH )
)

Month-over-Month Change =
[Total Sales] - [Previous Month Sales]

Month-over-Month Change % =
DIVIDE ( [Month-over-Month Change], [Previous Month Sales] )
```

Format sales, cost, tax, and gross-income measures as decimal numbers using a consistent number of decimal places. Apply percentage formatting to margin and month-over-month percentage. Confirm the source currency before using a currency symbol.

## 4. Suggested report pages

### Page 1 — Executive overview

- KPI cards: Total Sales, Total Orders, Units Sold, Gross Income, Average Rating.
- Line chart: Total Sales by Calendar[Year Month].
- Bar chart: Total Sales by Product line.
- Bar chart: Total Sales by City or Branch.
- Slicers: Date, Branch, City, Product line.

### Page 2 — Product performance

- Bar chart: Sales by Product line.
- Matrix: Product line by Branch with Sales, Units Sold, Gross Income, Average Rating.
- Slicers: Branch, City, Date.

### Page 3 — Customer and payment

- Column chart: Sales by Customer type.
- Column chart: Sales by Gender.
- Donut or bar chart: Sales by Payment.
- Cards: Average Order Value and Total Orders.

### Page 4 — Time analysis

- Line chart: Sales by Date.
- Column chart: Sales by Day Name.
- Column chart: Sales by Hour (create hour in Power Query or DAX from the Time field).
- Matrix: Branch by time of day, if that field has been added during preparation.

## 5. Validation checklist

Before publishing or sharing the report, compare card totals against the source and Python summary:

- Total Orders should be 1,000.
- Units Sold should be 5,510.
- Total Sales should be 322,966.75.
- Cost of Goods Sold should be 307,587.38.
- Gross Income should be 15,379.37.
- Average Rating should be approximately 6.97.

Small differences may result from data-type or rounding choices. Investigate any material discrepancy before sharing the report.

## 6. Interpretation cautions

This dataset contains three months of historical sample transactions. Treat the report as a portfolio case study, not as a current Walmart operational dashboard. Descriptive comparisons do not establish causal explanations.
