# Lab 3: Student Performance Tracking System

## Description
A Python application designed for instructors to track student performance. The system collects student names and letter grades, validates inputs, and provides options to view rosters, student totals, grade distributions, and percentage statistics.

---

## Program Structure
The application is organized into three separate modules:

- **`main.py`**: Entry point that initializes data structures (lists for names and grades) and orchestrates the input and output module calls.
- **`inputs.py`**: Handles user data collection, including input prompts for student counts, names, letter grades, input validation (ensuring valid grades A, B, C, D, or F), and batch entry options.
- **`outputs.py`**: Calculates statistics and presents an interactive menu allowing instructors to view specific class reporting metrics.

---

## How to Run
1. Ensure Python 3 is installed on your computer.
2. Open a terminal or command prompt in the directory where the project files are located.
3. Run the application:

```bash
python main.py
