# Walmart Sales Data Analysis

This case study analyzes a 1,000-row retail sales transaction dataset with MySQL. It includes the original CSV, a MySQL 8 database dump, and reusable SQL analysis queries.

## End-to-End Portfolio Project

The accompanying **Retail Sales Analytics** project expands this case study across Python, MySQL, and Power BI.

- [Open the Retail Sales Analytics project](retail-sales-analytics/)
- [Python analysis pipeline](retail-sales-analytics/analyze_sales.py)
- [Power BI dashboard build guide](retail-sales-analytics/powerbi_guide.md)
- [Data dictionary](retail-sales-analytics/data_dictionary.md)

The Python workflow reads the CSV in this folder and generates data-quality checks, KPI summaries, grouped CSV reports, and charts. See the project README for setup and run instructions.

## Source Files

- [Walmart sales CSV](WalmartSalesData.csv.csv)
- [MySQL 8 database dump](walmartsales_backup.sql)
- [Reusable SQL analysis queries](analysis_queries.sql)

## MySQL Setup

From this folder:

```bash
mysql -u root -p < walmartsales_backup.sql
mysql -u root -p walmartsales < analysis_queries.sql
```

The SQL dump creates the `walmartsales` database and `sales` table. MySQL 8.0 or later is recommended for CTE and window-function examples.

## Dataset Overview

The source CSV has 1,000 transaction rows and 17 source columns covering invoice, branch, city, customer type, gender, product line, unit price, quantity, tax, total, date/time, payment, COGS, gross margin percentage, gross income, and rating.

The data covers 1 January 2019 through 30 March 2019. It is a historical dataset for portfolio analysis, not current retail performance data.

## Author

**Sruthi Laya Perla**
