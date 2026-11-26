# Data Dictionary

Source: `WalmartSalesData.csv.csv` (17 source columns).

| Column | Meaning | Suggested Power BI / pandas type |
|---|---|---|
| Invoice ID | Unique transaction identifier | Text |
| Branch | Branch code (A, B, C) | Text |
| City | City associated with the branch | Text |
| Customer type | Member or Normal customer classification | Text |
| Gender | Recorded customer gender category | Text |
| Product line | Product category | Text |
| Unit price | Price per unit in source units | Decimal |
| Quantity | Units purchased | Whole number |
| Tax 5% | Tax amount recorded for the transaction | Decimal |
| Total | Transaction total recorded in source units | Decimal |
| Date | Transaction date | Date |
| Time | Transaction time | Time |
| Payment | Payment method | Text |
| cogs | Cost of goods sold | Decimal |
| gross margin percentage | Gross margin percentage field from source | Decimal |
| gross income | Gross income amount from source | Decimal |
| Rating | Customer rating | Decimal |

## Derived fields in the Python workflow

| Derived field | Definition |
|---|---|
| Year-Month | Transaction date formatted as YYYY-MM |
| Day Name | Weekday name from Date |
| Day Number | Weekday ordinal, Monday = 0 |
| Hour | Hour component parsed from Time |

## Data handling notes

- Invoice ID should be treated as an identifier, not a numeric measure.
- Date and Time should be parsed as date/time values before time-series analysis.
- The source file does not identify a currency symbol in the column definitions. Confirm its original metadata before applying a currency symbol.
- `gross margin percentage` is already included in the dataset. It is not the same as gross income amount.
- The Python workflow reports missing values, duplicate invoice identifiers, invalid dates, and numeric conversion problems before interpretation.
