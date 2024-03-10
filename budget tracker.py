import json

def load_data():
    try:
        with open('Sarvesh.expense', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'income': 0, 'expenses': []}

def save_data(data):
    with open('Sarvesh.expense', 'w') as file:
        json.dump(data, file)

def add_income(data):
    income = float(input("Enter income amount: "))
    data['income'] += income
    save_data(data)

def add_expense(data):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    data['expenses'].append({'category': category, 'amount': amount})
    save_data(data)

def calculate_budget(data):
    total_expenses = sum(expense['amount'] for expense in data['expenses'])
    remaining_budget = data['income'] - total_expenses
    return remaining_budget

def analyze_expenses(data):
    categories = {}
    for expense in data['expenses']:
        category = expense['category']
        amount = expense['amount']
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount
    return categories

def main():
    data = load_data()

    while True:
        print("\n1. Add Income\n2. Add Expense\n3. Calculate Budget\n4. Analyze Expenses\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            remaining_budget = calculate_budget(data)
            print(f"Remaining Budget: {remaining_budget}")
        elif choice == '4':
            categories = analyze_expenses(data)
            print("Expense Analysis:")
            for category, amount in categories.items():
                print(f"{category}: {amount}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
