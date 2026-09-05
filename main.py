#*****************************************************************************
#Author:            Nidhi Kairon
#Description:       This is a Banking program with options to print balance,
#                   make a deposit, and make a withdrawl
#Input:             continue2, str choice, float depositAmount,
#                   float withdrawalAmount
#Output:            withdrawalAmount, currentBalance
#*****************************************************************************

import valid as inputValidation

def main():
    user = True
    continue2 = ' '
    CurrentBalance = 0.0

    print("Welcome to the checking account\n")

    while user == True:
        CurrentBalance = inputValidation.choiceAndInput(CurrentBalance, continue2, user)
        user = inputValidation.continueChoice(continue2, user)

    print("\nYour Final Balance: ${:.2f}".format(CurrentBalance))
    print("Thank you for using this program!")

main()
