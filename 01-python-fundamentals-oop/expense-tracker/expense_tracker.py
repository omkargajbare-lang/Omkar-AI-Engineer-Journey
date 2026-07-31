from datetime import datetime


# -----------------------------
# Expense Functions
# -----------------------------

def add_expense(expense_list, expense_id, date, category, amount, description):
    expense = {
        "expense_id": expense_id,
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expense_list.append(expense)

    return "Expense added successfully"


def view_expenses(expense_list):
    if not expense_list:
        return "No expenses present."

    return expense_list


def calculate_total_expense(expense_list):
    total = 0

    for expense in expense_list:
        total += expense["amount"]

    return total


def calculate_total_by_category(expense_list, category):
    total = 0

    for expense in expense_list:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]

    return total


def modify_expense(expense_list, expense_id, new_amount):
    for expense in expense_list:
        if expense["expense_id"] == expense_id:
            expense["amount"] = new_amount
            return "Expense updated successfully"

    return "No such expense present"


def delete_expense(expense_list, expense_id):
    for expense in expense_list:
        if expense["expense_id"] == expense_id:
            expense_list.remove(expense)
            return "Expense deleted successfully"

    return "No such expense present"


# -----------------------------
# Input Validation Functions
# -----------------------------

def get_expense_date():
    while True:
        date_input = input(
            "Enter date of expense (YYYY-MM-DD): "
        ).strip()

        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input

        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD format.")


def get_expense_category():
    while True:
        category_input = input(
            "Enter expense category: "
        ).strip()

        if category_input == "":
            print("Category cannot be empty.")
            continue

        return category_input


def get_expense_amount():
    while True:
        try:
            amount_input = float(
                input("Enter expense amount: ")
            )

            if amount_input <= 0:
                print(
                    "Amount should be greater than 0."
                )
                continue

            return amount_input

        except ValueError:
            print(
                "Invalid amount. Please enter a valid number."
            )


def get_expense_description():
    return input(
        "Enter expense description: "
    ).strip()


def get_expense_id():
    while True:
        try:
            return int(
                input("Enter expense ID: ")
            )

        except ValueError:
            print(
                "Expense ID must be a valid integer."
            )


# -----------------------------
# Main Program
# -----------------------------

print("------ Welcome to the Expense Tracker! ------")

expense_list = []
next_expense_id = 1


while True:

    print(
        "\n1. Add Expense"
        "\n2. View All Expenses"
        "\n3. Calculate Total Expense"
        "\n4. Calculate Category Total"
        "\n5. Modify Expense"
        "\n6. Delete Expense"
        "\n7. Exit"
    )

    try:
        choice = int(input("\nEnter your choice: "))

    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 7.")
        continue

    # -------------------------
    # Add Expense
    # -------------------------

    if choice == 1:

        date_input = get_expense_date()
        category_input = get_expense_category()
        amount_input = get_expense_amount()
        desc_input = get_expense_description()

        message = add_expense(
            expense_list,
            next_expense_id,
            date_input,
            category_input,
            amount_input,
            desc_input
        )

        print(message)

        next_expense_id += 1

    # -------------------------
    # View Expenses
    # -------------------------

    elif choice == 2:

        expenses = view_expenses(expense_list)

        if isinstance(expenses, str):
            print(expenses)

        else:
            for expense in expenses:
                print(expense)

    # -------------------------
    # Calculate Total
    # -------------------------

    elif choice == 3:

        total_expense = calculate_total_expense(
            expense_list
        )

        print(f"Total Expense is: {total_expense:.2f}")

    # -------------------------
    # Category Total
    # -------------------------

    elif choice == 4:

        category_input = input(
            "Enter category: "
        ).strip()

        category_total = calculate_total_by_category(
            expense_list,
            category_input
        )

        print(
            f"Category Expense is: {category_total:.2f}"
        )

    # -------------------------
    # Modify Expense
    # -------------------------

    elif choice == 5:

        expense_id = get_expense_id()
        new_amount = get_expense_amount()

        modified_amount = modify_expense(
            expense_list,
            expense_id,
            new_amount
        )

        print(modified_amount)

    # -------------------------
    # Delete Expense
    # -------------------------

    elif choice == 6:

        expense_id = get_expense_id()

        delete_message = delete_expense(
            expense_list,
            expense_id
        )

        print(delete_message)

    # -------------------------
    # Exit
    # -------------------------

    elif choice == 7:

        print("Thank you for using Expense Tracker!")
        break

    else:

        print(
            "Incorrect input. Please select between 1 and 7."
        )