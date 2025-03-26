import json
from datetime import datetime

DATA_FILE = 'expenses.json'

def load_expenses():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    amount = float(input("Enter amount: $"))
    category = input("Enter category (Food, Bills, Transport, etc.): ")
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    for exp in expenses:
        print(f"{exp['date']} - {exp['category']} - ${exp['amount']} - {exp['description']}")

def total_expenses(expenses):
    total = sum(exp['amount'] for exp in expenses)
    print(f"Total Expenses: ${total}")

def main():
    expenses = load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            total_expenses(expenses)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
