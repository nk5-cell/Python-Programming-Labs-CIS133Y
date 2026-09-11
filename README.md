# Lab 4: US Census Bureau Popular Names Query

## Description
An Object-Oriented Python application that connects to an external SQL database (`pymssql`) to query US Census Bureau historical name data. The application prompts the user for a valid year and gender, queries the 20 most popular baby names matching the criteria, maps the raw database records into domain `Name` objects, and formats the results for output.

---

## Program Architecture
The project follows an Object-Oriented, layered architectural pattern:

- **`main.py`**: Presentation layer. Collects and validates user inputs (year between 1915–2014 and gender 'M'/'F'), invokes data fetching methods, and prints formatted output tables.
- **`lab4Name.py`**: Business logic / Entity layer. Defines the `Name` class with encapsulated private attributes (`__name`, `__year`, `__gender`, `__count`), getters/setters via `@property`, and a static factory method `readNames()` to map raw dictionary records into `Name` instances.
- **`lab4Database.py`**: Data Access Layer (DAL). Manages the database connection to the remote SQL Server using `pymssql` and executes parameterized SQL queries against the `NAMES` database.

---

## Prerequisites & Dependencies
- Python 3.x
- `pymssql` library (requires connection to the network hosting `cisdbss.pcc.edu`)

To install the database driver:
```bash
pip install pymssql
