expenses = []

def removeExpense():
    while True:
        listExpenses()
        print("What expense would you like to remove?")
        try:
            expenseToRemove = int(input("> "))
            if 0 <= expenseToRemove < len(expenses):  # Check if index is valid
                del expenses[expenseToRemove]
                print("Expense removed successfully.")
                break
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")

def updateExpense():
    while True:
        listExpenses()
        print("Which expense would you like to update?")
        try:
            expenseToUpdate = int(input("> "))
            if 0 <= expenseToUpdate < len(expenses):
                print("Do you want to update the amount or category? Enter 'amount' or 'category':")
                updateType = input("> ").lower()
                if updateType == 'amount':
                    print("Enter the new amount:")
                    while True:
                        try:
                            newAmount = float(input("> "))  # Convert input to float
                            expenses[expenseToUpdate]['amount'] = newAmount
                            print("Expense amount updated successfully.")
                            break
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                elif updateType == 'category':
                    print("Enter the new category:")
                    newCategory = input("> ")
                    expenses[expenseToUpdate]['category'] = newCategory
                    print("Expense category updated successfully.")
                else:
                    print("Invalid update type. Please enter 'amount' or 'category'.")
                break
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")

def addExpense():
    print("How much was this expense?")
    while True:
        try:
            amountToAdd = float(input("> "))  # Convert input to float
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("What category was this expense?")
    category = input("> ")
    expenses.append({'amount': amountToAdd, 'category': category})
    print("Expense added successfully.")

def calculateTotal():
    total = sum(expense['amount'] for expense in expenses)
    return total

def printMenu():
    print("Please choose from one of the following options...")
    print("1. Add A New Expense")
    print("2. Remove An Expense")
    print("3. Update An Expense")
    print("4. List All Expenses")

def listExpenses():
    if not expenses:
        print("\nYou have no expenses recorded.\n")
    else:
        print("\nHere is a list of your expenses...")
        print("------------------------------------")
        for index, expense in enumerate(expenses):
            print("#", index, " - ", expense['amount'], " - ", expense['category'])
        print("\nTotal amount:", calculateTotal(), "\n")

if __name__ == "__main__":
    while True:
        printMenu()
        optionSelected = input("> ")

        if optionSelected == "1":
            addExpense()
        elif optionSelected == "2":
            if not expenses:
                print("No expenses to remove.")
            else:
                removeExpense()
        elif optionSelected == "3":
            if not expenses:
                print("No expenses to update.")
            else:
                updateExpense()
        elif optionSelected == "4":
            listExpenses()
        else:
            print("Invalid input. Please try again.")
