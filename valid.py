import calculations

def continueChoice(continue2, user):
    continue2 = input("\nPress 'y' to continue, or any other key to exit: ").lower()
    if continue2 == 'y':
        return True
    else:
        return False

def choiceAndInput(currentBalance, continue2, user):
    try:
        choice = str(input("Enter 'd' for deposit, 'w' withdraw, 'c' for your account balance: ")).lower()
    except ValueError:
        print("Invalid input, please enter again.")

    if choice == 'd':
        try:
            depositAmount = float(input("Enter an amount to deposit: "))
            currentBalance = calculations.deposit(currentBalance, depositAmount)
            print(f"You have deposit: ${currentBalance:.2f}")
        except ValueError:
            print("Invalid input, please enter again.")
    elif choice == 'w':
        try:
            withdrawalAmount = float(input("Enter an amount to withdrawal: "))
            if ((currentBalance - withdrawalAmount) < 0):
                print("You do not have enough money to withdraw!")
            else:
                print(f"You have withdrawal: ${withdrawalAmount:.2f}")
                currentBalance = calculations.balance(withdrawalAmount, currentBalance)
        except ValueError:
            print("Invalid input.")
    elif choice == 'c':
            print(f"You current balance: ${currentBalance:.2f}")
    else:
        print("Invalid input.")
    return currentBalance
