 Walmart Sales Data Analysis using MySQL

## 📌 Project Overview

This project focuses on analyzing **Walmart sales transaction data using MySQL** to understand sales performance, product performance, branch performance, customer behavior, and sales trends.

The main objective is to identify **top-performing products and branches, customer purchasing patterns, sales trends, and profitability**, and use these findings to understand how sales strategies can be improved and optimized.

The dataset contains sales transactions from three Walmart branches located in **Mandalay, Yangon, and Naypyitaw**, with **1,000 records and 17 columns**.

---

## 🎯 Project Objectives

The major objectives of this project are:

* Analyze overall Walmart sales performance.
* Identify the best-performing product lines.
* Identify branches and cities generating the highest revenue.
* Understand customer purchasing behavior.
* Analyze customer types and gender distribution.
* Identify popular payment methods.
* Analyze sales by day, month, and time of day.
* Evaluate customer ratings.
* Analyze COGS, VAT, gross income, and gross margin.
* Identify areas that require improvement.
* Generate actionable business insights.

---

# 📊 Dataset

The dataset contains **1,000 rows and 17 columns**.

| Column             | Description                     | Data Type     |
| ------------------ | ------------------------------- | ------------- |
| `invoice_id`       | Unique invoice ID for each sale | VARCHAR       |
| `branch`           | Walmart branch                  | VARCHAR       |
| `city`             | Location of the branch          | VARCHAR       |
| `customer_type`    | Type of customer                | VARCHAR       |
| `gender`           | Gender of customer              | VARCHAR       |
| `product_line`     | Product category                | VARCHAR       |
| `unit_price`       | Price of each product           | DECIMAL       |
| `quantity`         | Quantity purchased              | INT           |
| `tax_pct`          | Tax percentage                  | FLOAT         |
| `total`            | Total transaction value         | DECIMAL       |
| `date`             | Date of purchase                | DATE/DATETIME |
| `time`             | Time of purchase                | TIME          |
| `payment`          | Payment method                  | VARCHAR       |
| `cogs`             | Cost of goods sold              | DECIMAL       |
| `gross_margin_pct` | Gross margin percentage         | FLOAT         |
| `gross_income`     | Gross income                    | DECIMAL       |
| `rating`           | Customer rating                 | FLOAT         |

---

# 🛠️ Tools & Technologies

* **MySQL**
* **MySQL Workbench**
* **CSV**

### SQL Skills Demonstrated

* Data Cleaning
* Data Validation
* Feature Engineering
* Exploratory Data Analysis
* Aggregate Functions
* `GROUP BY`
* `HAVING`
* `ORDER BY`
* `CASE`
* Subqueries
* CTEs
* Window Functions
* `RANK()`
* Date Functions
* Time Functions
* Business KPI Analysis

---

# 🔄 Project Approach

The project follows four major stages:

```text
Raw Sales Data
      ↓
Database & Table Creation
      ↓
Data Wrangling
      ↓
Feature Engineering
      ↓
Exploratory Data Analysis
      ↓
Business Analysis
      ↓
Insights & Recommendations
```

---

# 1️⃣ Data Wrangling

The first stage involved inspecting the dataset and preparing it for analysis.

### Steps performed

* Created a MySQL database.
* Created the `sales` table.
* Defined appropriate data types.
* Used constraints such as `NOT NULL`.
* Checked the dataset for missing values.
* Prepared the data for analysis.

The original project approach specifically included database creation, table creation, data insertion, and checking columns for NULL values.

---

# 2️⃣ Feature Engineering

Three additional columns were created from existing date and time information:

### `time_of_day`

Categorizes transactions into:

* Morning
* Afternoon
* Evening

This helps identify which part of the day has the highest sales activity.

### `day_name`

Extracts the day of the week from the transaction date.

This helps identify the busiest days.

### `month_name`

Extracts the month from the transaction date.

This helps analyze monthly sales and profitability.

These feature-engineering steps are part of the original project methodology.

---

# 3️⃣ Exploratory Data Analysis

EDA was performed to answer business questions related to:

* Product performance
* Sales trends
* Customer behavior
* Branch performance
* Payment methods
* Customer ratings
* Revenue
* Profitability

The original analysis is organized into **Product Analysis, Sales Analysis, and Customer Analysis**.

---

# 🏷️ Product Analysis

### Business Questions

1. How many unique product lines are there?
2. What is the most selling product line?
3. What is the total revenue by month?
4. Which month has the largest COGS?
5. Which product line generates the largest revenue?
6. Which city generates the largest revenue?
7. Which product line has the largest VAT?
8. Which product lines perform above average?
9. Which branch sells more products than average?
10. What is the most common product line by gender?
11. What is the average rating for each product line?

These questions follow the product-analysis scope defined in the source material.
---

# 💰 Sales Analysis

The sales analysis focuses on understanding sales trends and the effectiveness of different sales strategies.

### Business Questions

* How many sales are made during each time of day?
* Which customer type generates the most revenue?
* Which city has the highest average VAT?
* Which customer type pays the most VAT?
* Which month generates the highest revenue?
* Which day generates the highest sales?

The project uses these questions to understand sales trends and identify areas where sales strategies may be improved.

---

# 👥 Customer Analysis

The customer analysis focuses on customer segments, purchasing behavior, gender distribution, ratings, and profitability.

### Business Questions

1. How many unique customer types are there?
2. How many unique payment methods are there?
3. What is the most common customer type?
4. Which customer type buys the most?
5. Which gender represents the majority of customers?
6. What is the gender distribution by branch?
7. Which time of day receives the highest average rating?
8. Which time of day receives the highest rating by branch?
9. Which day has the best average rating?
10. Which day has the best average rating by branch?

These questions are based on the customer-analysis section of the original project.

---

# 💵 Revenue & Profitability Analysis

The project also analyzes the relationship between:

* Unit Price
* Quantity
* COGS
* VAT
* Total Revenue
* Gross Income
* Gross Margin

### COGS

```text
COGS = Unit Price × Quantity
```

### VAT

```text
VAT = 5% × COGS
```

### Total Revenue

```text
Total Revenue = COGS + VAT
```

### Gross Income

```text
Gross Income = Total Revenue − COGS
```

### Gross Margin

```text
Gross Margin = Gross Income / Total Revenue
```

These calculations and relationships are defined in the original project documentation.

---

# 🔍 Example Calculation

For one sample transaction:

```text
Unit Price = 45.79
Quantity = 7
```

### Step 1 — Calculate COGS

```text
45.79 × 7 = 320.53
```

### Step 2 — Calculate VAT

```text
5% × 320.53 = 16.0265
```

### Step 3 — Calculate Total

```text
320.53 + 16.0265 = 336.5565
```

### Step 4 — Calculate Gross Margin

```text
16.0265 / 336.5565 ≈ 4.7619%
```

This example is included in the source project documentation.

---

# 📈 Key Analysis Areas

The project analyzes Walmart sales from multiple business perspectives:

| Analysis Area | Key Focus                          |
| ------------- | ---------------------------------- |
| Product       | Product-line performance           |
| Sales         | Sales trends and revenue           |
| Customer      | Customer segments and behavior     |
| Branch        | Branch-level performance           |
| City          | Geographic performance             |
| Payment       | Payment preferences                |
| Time          | Morning/Afternoon/Evening trends   |
| Day           | Day-of-week performance            |
| Month         | Monthly sales and profit           |
| Rating        | Customer satisfaction              |
| Profitability | COGS, VAT, gross income and margin |

---

# 📌 Key Business Questions

The project ultimately attempts to answer:

### Product Performance

* Which products sell the most?
* Which product lines generate the highest revenue?
* Which products need improvement?

### Sales Performance

* Which month has the highest revenue?
* Which day has the highest sales?
* What time of day generates the most sales?

### Customer Behavior

* Which customer type generates the most revenue?
* Which gender purchases more?
* Which payment method is most popular?
* Which customers give the highest ratings?

### Branch Performance

* Which branch performs best?
* Which city generates the highest revenue?
* Which branch has the strongest customer satisfaction?

### Profitability

* What is the total COGS?
* What is the gross income?
* What is the gross margin?
* Which product line is the most profitable?

---

# 💡 Business Insights

The analysis can be used to identify:

* Top-performing product categories.
* Underperforming product categories.
* High-value customer segments.
* Strong and weak branches.
* Peak sales periods.
* Popular payment methods.
* Customer satisfaction patterns.
* Monthly sales trends.
* Revenue and profitability opportunities.

---

# 📁 Project Structure

```text
Walmart-Sales-Analysis/
│
├── data/
│   └── WalmartSalesData.csv
│
├── sql/
│   ├── 01_database_setup.sql
│   ├── 02_data_cleaning.sql
│   ├── 03_feature_engineering.sql
│   ├── 04_product_analysis.sql
│   ├── 05_sales_analysis.sql
│   ├── 06_customer_analysis.sql
│   ├── 07_branch_analysis.sql
│   ├── 08_profitability_analysis.sql
│   └── 09_advanced_analysis.sql
│
└── README.md
```

---

# 🎓 Skills Demonstrated

### Technical

**MySQL | SQL | Data Cleaning | Feature Engineering | EDA | CTEs | Subqueries | Window Functions | Date & Time Analysis**

### Analytical

**Business Analysis | KPI Analysis | Sales Analysis | Product Analysis | Customer Segmentation | Branch Analysis | Profitability Analysis | Business Insights**

---

# 🚀 Conclusion

This project demonstrates how **MySQL and SQL can be used to transform raw sales transaction data into meaningful business insights**.

By analyzing products, branches, customers, sales trends, payment methods, ratings, revenue, and profitability, the project provides a structured approach to understanding Walmart's sales performance.

The analysis can help businesses make better decisions related to:

* Product strategy
* Sales strategy
* Customer retention
* Branch performance
* Promotions
* Inventory planning
* Profitability improvement


