import json
import os
import PySimpleGUI as sg

class ExpenseTracker:
    def __init__(self, data_file="expenses.json"):
        self.data_file = data_file
        self.expenses = self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {"expenses": []}

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.expenses, file, indent=2)

    def add_expense(self, amount, description, category, date):
        expense = {"amount": amount, "description": description, "category": category, "date": date}
        self.expenses["expenses"].append(expense)
        self.save_data()

    def get_monthly_summary(self):
        monthly_summary = {}
        for expense in self.expenses["expenses"]:
            month_year = expense.get("date", "Unknown")[:7]
            if month_year not in monthly_summary:
                monthly_summary[month_year] = 0
            monthly_summary[month_year] += expense["amount"]
        return monthly_summary

    def get_category_summary(self):
        category_summary = {}
        for expense in self.expenses["expenses"]:
            category = expense["category"]
            if category not in category_summary:
                category_summary[category] = 0
            category_summary[category] += expense["amount"]
        return category_summary

    def show_expenses(self):
        return self.expenses["expenses"]

#FROM HERE THE UI OF THE PROGRAM STARTS
def main():
    tracker = ExpenseTracker()

    layout = [
        [sg.Text("Expense Tracker", size=(30, 1), font=("Helvetica", 25), justification="center")],
        [sg.Button("Add Expense"), sg.Button("View Monthly Summary"), sg.Button("View Category Summary"), sg.Button("View All Expenses"), sg.Button("Exit")]
    ]

    window = sg.Window("Expense Tracker", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        elif event == "Add Expense":
            add_expense_layout = [
                [sg.Text("Amount"), sg.InputText(key="amount")],
                [sg.Text("Description"), sg.InputText(key="description")],
                [sg.Text("Category"), sg.InputText(key="category")],
                [sg.Text("Date"), sg.InputText(key="date"), sg.CalendarButton("Select Date", target="date", format="%Y-%m-%d")],
                [sg.Button("Submit"), sg.Button("Cancel")]
            ]
            add_expense_window = sg.Window("Add Expense", add_expense_layout)
            while True:
                add_event, add_values = add_expense_window.read()
                if add_event == sg.WINDOW_CLOSED or add_event == "Cancel":
                    break
                elif add_event == "Submit":
                    try:
                        amount = float(add_values["amount"])
                        description = add_values["description"]
                        category = add_values["category"]
                        date = add_values["date"]
                        tracker.add_expense(amount, description, category, date)
                        sg.popup("Expense added successfully!")
                        break
                    except ValueError:
                        sg.popup("Invalid input. Please enter valid data.")
            add_expense_window.close()
        elif event == "View Monthly Summary":
            monthly_summary = tracker.get_monthly_summary()
            summary_layout = [[sg.Text(f"{month_year}: ₹{total_amount:.2f}")] for month_year, total_amount in monthly_summary.items()]
            summary_layout.append([sg.Button("Close")])
            summary_window = sg.Window("Monthly Summary", summary_layout)
            summary_window.read()
            summary_window.close()
        elif event == "View Category Summary":
            category_summary = tracker.get_category_summary()
            category_layout = [[sg.Text(f"{category}: ₹{total_amount:.2f}")] for category, total_amount in category_summary.items()]
            category_layout.append([sg.Button("Close")])
            category_window = sg.Window("Category Summary", category_layout)
            category_window.read()
            category_window.close()
        elif event == "View All Expenses":
            expenses = tracker.show_expenses()
            expenses_layout = [
                [sg.Text(f"Amount: ₹{expense['amount']}, Description: {expense['description']}, Category: {expense['category']}, Date: {expense.get('date', 'Unknown')}")] 
                for expense in expenses
            ]
            expenses_layout.append([sg.Button("Close")])
            expenses_window = sg.Window("All Expenses", expenses_layout)
            expenses_window.read()
            expenses_window.close()

    window.close()

if __name__ == "__main__":
    main()


