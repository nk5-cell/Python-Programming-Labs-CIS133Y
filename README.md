# CIS 133Y: Python Programming - Comprehensive Lab Portfolio

**Author:** Nidhi Kairon

**Course:** CIS133Y Submissions

**Repository Contents:** Labs 1 through 5

---

## Table of Contents

1. [Lab 1: Food Items Total and Tip Calculator]
2. [Lab 2: Modular Checking Account System]
3. [Lab 3: Student Performance Tracking System]
4. [Lab 4: US Census Bureau Popular Names Query]
5. [Lab 5: US Census Data Visualization with Pandas & Matplotlib]
6. [Global Setup & Dependencies]

---

## Lab 1: Food Items Total and Tip Calculator

### Description

A Python CLI application that prompts the user to input food items along with their respective prices, computes the running total cost, and provides options to calculate suggested gratuity (10%, 15%, or 20%).

This program collects a list of food items and costs through an interactive console interface. It allows users to continuously add items across multiple rounds before finalizing the bill. Once item entry is complete, the program presents the subtotal and gives the user an optional choice to calculate tip amounts based on standard percentages.

### Key Features

* **Interactive Item Entry:** Allows users to specify how many items they want to enter and continuously add more in subsequent passes.
* **Dynamic Cost Tracking:** Keeps a running tally of food items and sums up total expenditures.
* **Tip Calculation:** Offers preset options for gratuity:
* Option `A`: 10% tip
* Option `B`: 15% tip
* Option `C`: 20% tip


* **Formatted Currency Output:** Displays formatted currency values rounded to two decimal places.

### Inputs & Outputs

* **Inputs**:
* `totalItems` (*int*): Number of food items to add per loop pass.
* `foodItems` (*str*): Name of each food item.
* `foodItemsCost` (*float*): Cost of each individual food item.
* `continuePrompt` (*str*): Option (`Y`/`N`) to continue adding additional items.
* `tip` (*str*): Option (`Y`/`N`) to apply a gratuity choice.
* `amountTip` (*str*): Selected tip tier (`A`, `B`, or `C`).


* **Outputs**:
* Subtotal (`totalCost`)
* Tip amount (`tipAmountCalculated`)
* Combined total (`totalCost + tipAmountCalculated`)



---

## Lab 2: Modular Checking Account System

### Description

A modular Python program that simulates basic checking account management. Users can check their balance, deposit funds, or withdraw funds with real-time balance tracking and overdraft validation.

### Program Structure

The project is split into three main modules:

* **`main.py`**: Controls the program flow, initializes account balance, manages the main loop, and displays final program outputs.
* **`valid.py`**: Handles user menu selections, input prompts, error handling (e.g., catching `ValueError`), overdraft checks, and continue/exit prompts.
* **`calculations.py`**: Contains helper functions to perform mathematical operations for deposits and withdrawals.

### Features & Usage

1. **Deposit (`d`)**: Enter a float value to add funds to the current account balance.
2. **Withdraw (`w`)**: Enter a float value to withdraw funds. The program checks to prevent the balance from going below $0.00.
3. **Check Balance (`c`)**: Prints the current available account balance formatted to two decimal places.
4. **Loop / Exit**: Prompted after every transaction (`y` to continue, any other key to exit and show the final balance).

---

## Lab 3: Student Performance Tracking System

### Description

A Python application designed for instructors to track student performance. The system collects student names and letter grades, validates inputs, and provides options to view rosters, student totals, grade distributions, and percentage statistics.

### Program Structure

The application is organized into three separate modules:

* **`main.py`**: Entry point that initializes data structures (lists for names and grades) and orchestrates the input and output module calls.
* **`inputs.py`**: Handles user data collection, including input prompts for student counts, names, letter grades, input validation (ensuring valid grades A, B, C, D, or F), and batch entry options.
* **`outputs.py`**: Calculates statistics and presents an interactive menu allowing instructors to view specific class reporting metrics.

### Menu Options

1. **Display Class Roster**: Outputs all student names paired with their respective letter grades.
2. **Display Total Number of Students**: Shows the total count of enrolled students in the system.
3. **Display Number of Students per Letter Grade**: Displays the exact count of A, B, C, D, and F grades.
4. **Display Percentage of Each Letter Grade**: Calculates and formats the percentage distribution for each letter grade.
5. **Exit Program**: Terminates the program session.

---

## Lab 4: US Census Bureau Popular Names Query

### Description

An Object-Oriented Python application that connects to an external SQL database (`pymssql`) to query US Census Bureau historical name data. The application prompts the user for a valid year and gender, queries the 20 most popular baby names matching the criteria, maps the raw database records into domain `Name` objects, and formats the results for output.

### Program Architecture

The project follows an Object-Oriented, layered architectural pattern:

* **`main.py`**: Presentation layer. Collects and validates user inputs (year between 1915–2014 and gender 'M'/'F'), invokes data fetching methods, and prints formatted output tables.
* **`lab4Name.py`**: Business logic / Entity layer. Defines the `Name` class with encapsulated private attributes (`__name`, `__year`, `__gender`, `__count`), getters/setters via `@property`, and a static factory method `readNames()` to map raw dictionary records into `Name` instances.
* **`lab4Database.py`**: Data Access Layer (DAL). Manages the database connection to the remote SQL Server using `pymssql` and executes parameterized SQL queries against the `NAMES` database.

---

## Lab 5: US Census Data Visualization with Pandas & Matplotlib

### Description

A data analysis and visualization program that extracts historical census data for the name **"Anna"** from an external SQL database. Using **Pandas**, the data is transformed between long and wide formats and analyzed to calculate demographic proportions. Using **Matplotlib**, the program generates line plots to visualize historical trends in name frequency and gender proportions over time.

### Program Architecture & Data Pipeline

1. **Database Querying**: Connects to the SQL Server database (`NAMES` on `cisdbss.pcc.edu`) using `pymssql` and joins relational tables (`year_gender_totals`, `name_counts`, `names`) to pull all records for the name "Anna".
2. **Data Wrangling (Pandas)**:
* Loads raw query results into a Pandas Dataframe (`anna_data_long`).
* Pivots the dataset from long to wide format (`anna_data_wide`) to split female (`F`) and male (`M`) counts into distinct columns by year.
* Calculates a derived feature: `Percent Female` ($100 \times \frac{F}{F + M}$).
* Reshapes data using `melt()` to demonstrate long-format conversion (`ld`).


3. **Data Visualization (Matplotlib)**:
* **Plot 1**: Historical count of female vs. male babies named Anna over time.
* **Plot 2**: Percentage of babies named Anna who were female over time.



---

## Global Setup & Dependencies

### Prerequisites

* **Python Version**: Python 3.x installed across your system environment.
* **Network Access**: An active network or VPN connection to reach `cisdbss.pcc.edu` for database access in Labs 4 and 5.

### Installation

Install all required third-party packages for the portfolio via `pip`:

```bash
pip install pymssql pandas matplotlib

```

### Running the Labs

Execute any lab by navigating to its directory in your terminal and running the entry point module:

```bash
# Run Lab 1
python lab1.py

# Run Lab 2
python main.py

# Run Lab 3
python main.py

# Run Lab 4
python main.py

# Run Lab 5
python lab5.py

```
