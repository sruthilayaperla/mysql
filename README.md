# MySQL Data Analytics Portfolio

A practical SQL portfolio containing a Walmart sales analysis dataset and a Swiggy dataset. The Walmart case study includes a MySQL 8 database export and a companion set of reusable analysis queries.

## Projects

### 1. Walmart Sales Analysis

**Files**
- [Project notes](Walmart%20sales/Readme.Md)
- [MySQL database dump](Walmart%20sales/walmartsales_backup.sql)
- [Companion SQL analysis queries](Walmart%20sales/analysis_queries.sql)
- [Source CSV](Walmart%20sales/WalmartSalesData.csv.csv)

The dump creates the `walmartsales` database table named `sales`. Its columns cover invoice, branch, city, customer type, gender, product line, unit price, quantity, tax, total, date/time, payment, cost of goods sold, gross income, rating, and derived time fields.

**Load the database**

Using the MySQL command-line client from the repository root:

```bash
mysql -u root -p < "Walmart sales/walmartsales_backup.sql"
```

Then open a MySQL session and run:

```sql
USE walmartsales;
SELECT COUNT(*) AS invoice_count FROM sales;
```

Run the companion analysis file after loading the dump:

```bash
mysql -u root -p walmartsales < "Walmart sales/analysis_queries.sql"
```

The SQL file includes KPI summaries, product and branch comparisons, payment/customer breakdowns, time-based analysis, ranking, and window-function examples.

### 2. Swiggy Dataset

- [Swiggy CSV dataset](casestudy-swiggy/Swiggy.csv)

This folder currently provides the source dataset. A separate SQL schema, analysis notebook, and documented findings have not yet been added.

## Skills Demonstrated

- SQL querying, filtering, grouping, and aggregation
- Business KPI calculation and sales analysis
- Joins/CTEs/window-function practice in the companion query file
- Working with CSV data and MySQL database exports
- Translating transaction data into business questions

## Suggested Analysis Questions

1. Which product lines generate the highest sales?
2. Which branches and cities contribute most to revenue?
3. How do payment methods and customer types compare?
4. Which days and time periods have the most sales?
5. How do product ratings differ by product line?
6. How does each month's sales compare with the previous month?

## Requirements

- MySQL 8.0 or later is recommended for the window-function examples.
- Use the MySQL client or MySQL Workbench to restore the SQL dump.
- The CSV files can be inspected with a spreadsheet or a data-analysis tool.

## Data and Reproducibility

The Walmart SQL dump contains the table definition and rows needed to reproduce the queries. Query outputs can vary if the source data is changed. No performance, business-impact, or predictive-accuracy claims are made in this repository.

## Author

**Sruthi Laya Perla**
