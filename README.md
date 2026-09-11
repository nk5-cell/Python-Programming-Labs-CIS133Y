# Lab 2: Banking Program

## Description
A modular Python program that simulates basic checking account management. Users can check their balance, deposit funds, or withdraw funds with real-time balance tracking and overdraft validation.

---

## Program Structure
The project is split into three main modules:

- **`main.py`**: Controls the program flow, initializes account balance, manages the main loop, and displays final program outputs.
- **`valid.py`**: Handles user menu selections, input prompts, error handling (e.g., catching `ValueError`), overdraft checks, and continue/exit prompts.
- **`calculations.py`**: Contains helper functions to perform mathematical operations for deposits and withdrawals.

---

## How to Run
1. Make sure Python 3 is installed on your system.
2. Open a terminal/command prompt in the directory containing the source files.
3. Execute the program using:

```bash
python main.py
