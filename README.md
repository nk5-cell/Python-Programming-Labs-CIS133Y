# Lab 5: US Census Data Visualization with Pandas & Matplotlib

## Description
A data analysis and visualization program that extracts historical census data for the name **"Anna"** from an external SQL database. Using **Pandas**, the data is transformed between long and wide formats and analyzed to calculate demographic proportions. Using **Matplotlib**, the program generates line plots to visualize historical trends in name frequency and gender proportions over time.

---

## Program Architecture & Data Pipeline
The application demonstrates an end-to-end data processing workflow:

1. **Database Querying**: Connects to the SQL Server database (`NAMES` on `cisdbss.pcc.edu`) using `pymssql` and joins relational tables (`year_gender_totals`, `name_counts`, `names`) to pull all records for the name "Anna".
2. **Data Wrangling (Pandas)**:
   - Loads raw query results into a Pandas Dataframe (`anna_data_long`).
   - Pivots the dataset from long to wide format (`anna_data_wide`) to split female (`F`) and male (`M`) counts into distinct columns by year.
   - Calculates a derived feature: `Percent Female` ($100 \times \frac{F}{F + M}$).
   - Reshapes data using `melt()` to demonstrate long-format conversion (`ld`).
3. **Data Visualization (Matplotlib)**:
   - **Plot 1**: Historical count of female vs. male babies named Anna over time.
   - **Plot 2**: Percentage of babies named Anna who were female over time.

---

## Prerequisites & Dependencies
- Python 3.x
- `pandas`
- `matplotlib`
- `pymssql`

To install required packages:
```bash
pip install pandas matplotlib pymssql
