#*****************************************************************************
#Author:            Nidhi Kairon
#Description:       This program Prompt the user for a list of food items and
#                   their cost, and when they are done, print the total and
#                   calculate suggested tip amounts of 10%, 15%, and 20%.
#Input:             int totalItems, str foodItems, float foodItemsCost,
#                   str continuePrompt, str tip, str amountTip
#Output:            tipAmountCalculated, totalCost
#Sources:           Lab 3 Assignment Instruction, Module 3 Lessons
#*****************************************************************************

#variables for this program
numItems = 0
totalItems = 0
runLoop = 0
foodItemsCost = 0
totalCost = 0.0
tipAmountCalculated = 0.0
foodItems = ' '
continuePrompt = ' '
tip = ' '
amountTip = ' '
runLoopCondition = True

#display welcome message
print("Welcome to 'Food Items Total and Tip Calculator' program!")
print()
#outer loop if they want to continue adding more items
while runLoopCondition == True:
        #this conditions inputs the prompt based on if the user wants to add more items
        # or if they are adding it for the first time
        if runLoop < 1:
            totalItems = int(input("Enter the number for amount of food items you want to add: "))
        elif runLoop >= 1:
            totalItems = int(input("Enter the number for amount of food items you want to continue adding: "))

        #inner loop to input the food item name and its cost
        #inner loop runs based on the items they wish to add to their list
        for outLoop in range(0, totalItems):
            foodItems = str(input("Enter the name of food item [" + str(numItems + 1) + "]: "))
            foodItemsCost = float(input("Enter the cost of " + foodItems + ": $"))
            totalCost += foodItemsCost
            numItems += 1

        #this inputs the condition for outerloop to keep running or not
        continuePrompt = str(input("Enter 'Y' if you want to continue adding more items or press any key to exit: "))
        if continuePrompt == "Y" or continuePrompt == "y":
            runLoopCondition = True
            runLoop += 1
        else:
            runLoopCondition = False

#display the total cost
print("Your total cost is: $" + "{:.2f}".format(totalCost))

#as if the user wants to tip
tip = str(input("Do you want to tip [Enter 'Y' for Yes or 'N' for No]: "))
if tip == "Y" or tip == "y":
    print("Enter:")
    print("'A' for 10% tip from your total cost")
    print("'B' for 15% tip from your total cost")
    print("'C' for 20% tip from your total cost")
    amountTip = str(input())

#calculates tip
if amountTip == "A" or amountTip == "a":
    tipAmountCalculated = (totalCost * 0.10)
elif amountTip == "B" or amountTip == "b":
    tipAmountCalculated = (totalCost * 0.15)
if amountTip == "C" or amountTip == "c":
    tipAmountCalculated = (totalCost * 0.20)

#display calculated tip
print("Your Calculated tip is: $" + "{:.2f}".format(tipAmountCalculated))
print()
#display end message with calculated amount
print("Thank you for using our program!")
print("---------------------------------")
print("You total cost with Calculated tip is: $" + "{:.2f}".format(totalCost + tipAmountCalculated))
print("---------------------------------")


