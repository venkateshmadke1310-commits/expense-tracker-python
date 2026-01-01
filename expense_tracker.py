filename = "expenses.txt"

def load_expenses():
    expenses = []

    try:
        with open(filename, "r") as file:
            for line in file:
                date, category, amount, note = line.strip().split("|")
                expenses.append({
                    "date" : date,
                    "category" : category,
                    "amount" : float(amount),
                    "note" : note
                })

    except FileNotFoundError:
        pass

    return expenses

def save_expenses(expenses):
    with open(filename, "w") as file:
        for exp in expenses:
            line = f"{exp['date']}|{exp['category']}|{exp['amount']}|{exp['note']}\n"
            file.write(line)
             
def add_expense(expenses):
    exp_date = input("Enter Date (YYYY-MM-DD): ")
    exp_category = input("Enter Category: ")
    exp_amount = float(input("Enter Amount: "))
    exp_note = input("Enter Note: ")

    expenses.append({
        "date" : exp_date,
        "category" : exp_category,
        "amount" : exp_amount,
        "note" : exp_note
    })
    save_expenses(expenses)
    print("Expense added successfully.")

def view_expenses(expenses):
    if not expenses:
        print("No Expenses found.")
        return
    
    print("\n---Expense List---")
    for expense in expenses:
        print(f"Date     : {expense['date']}")
        print(f"Category : {expense['category']}")
        print(f"amount   : {expense['amount']}")
        print(f"note     : {expense['note']}")
        print("-" * 20)

def search_expense(expenses):
    keyword = input("Enter date or category to search: ").lower()
    found = False

    for expense in expenses:
        if keyword in expense["date"].lower() or keyword in expense["category"].lower():
            print(f"Date     : {expense['date']}")
            print(f"Category : {expense['category']}")
            print(f"Amount   : {expense['amount']}")
            print(f"note     : {expense['note']}")
            found = True

    if not found:
        print("No matching expenses found.")

def update_expense(expenses):
    keyword = input("Enter date or category to update: ").lower()
    found = False
    
    for expense in expenses:
      if keyword in expense["date"].lower() or keyword in expense["category"].lower():
        new_amount = input("Enter New Amount(leave blank to remain as it is): ")
        new_note = input("Enter New Note(leave blank to remain as it is): ")

        if new_amount:
            expense['amount'] = float(new_amount)
        
        if new_note:
            expense['note'] = new_note

        save_expenses(expenses)
        print("Expense updated successfully.")
        found = True
        return
        

    if not found:
        print("No matching expenses found. ")

def delete_expense(expenses):
    keyword = input("Enter date or category to delete expense: ").lower()
    found = False

    for expense in expenses:
        if keyword in expense["date"].lower() or keyword in expense["category"].lower():
            expenses.remove(expense)
            save_expenses(expenses)
            print("Expense deleted successfully.")
            found = True
            return
        
    if not found:
        print("No matching expenses found.")

def category_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return
    
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("\n--Category-wise Summary--")
    for category, amount in summary.items():
        print(f"{category} : {amount}")

def monthly_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return
    
    month = input("Enter month (YYYY-MM): ")
    total = 0

    for expense in expenses:
        if expense['date'].startswith(month):
            total += expense["amount"]

    print(f"\nTotal expense for {month}: {total}")

def menu():
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Category Summary")
    print("7. Monthly Summary")
    print("8. Exit")

expenses = load_expenses()

while True:
        menu()
        choice = input("Enter your choice (1-8): ")


        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            search_expense(expenses)

        elif choice == "4":
            update_expense(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            category_summary(expenses)

        elif choice == "7":
            monthly_summary(expenses)

        elif choice == "8":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("invalid choice. Please try again.")




    
