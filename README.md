# Lab 1: Food Items Total and Tip Calculator

A Python CLI application that prompts the user to input food items along with their respective prices, computes the running total cost, and provides options to calculate suggested gratuity (10%, 15%, or 20%).

---

## Program Description

This program collects a list of food items and costs through an interactive console interface. It allows users to continuously add items across multiple rounds before finalizing the bill. Once item entry is complete, the program presents the subtotal and gives the user an optional choice to calculate tip amounts based on standard percentages.

---

## Features

- **Interactive Item Entry:** Allows users to specify how many items they want to enter and continuously add more in subsequent passes.
- **Dynamic Cost Tracking:** Keeps a running tally of food items and sums up total expenditures.
- **Tip Calculation:** Offers preset options for gratuity:
  - Option `A`: 10% tip
  - Option `B`: 15% tip
  - Option `C`: 20% tip
- **Formatted Currency Output:** Displays formatted currency values rounded to two decimal places.

---

## Inputs & Outputs

### Inputs
- `totalItems` *(int)*: Number of food items to add per loop pass.
- `foodItems` *(str)*: Name of each food item.
- `foodItemsCost` *(float)*: Cost of each individual food item.
- `continuePrompt` *(str)*: Option (`Y`/`N`) to continue adding additional items.
- `tip` *(str)*: Option (`Y`/`N`) to apply a gratuity choice.
- `amountTip` *(str)*: Selected tip tier (`A`, `B`, or `C`).

### Outputs
- Subtotal (`totalCost`)
- Tip amount (`tipAmountCalculated`)
- Combined total (`totalCost + tipAmountCalculated`)

---

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Running the Program

1. Open your terminal or command prompt.
2. Navigate to the folder containing `lab1.py`:
   ```bash
   cd path/to/your/lab1
