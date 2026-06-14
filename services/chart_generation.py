import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import os

def save_expense_chart(transactions):
    summary = {}

    for t in transactions:
        if t.type == "expense":

            if t.category not in summary:
                summary[t.category] = 0

            summary[t.category] += t.amount

    if not summary:
        return

    categories = list(summary.keys())
    values = list(summary.values()) 

    plt.figure(figsize=(6, 4))

    plt.pie(
        values,
        labels=categories,
        autopct="%1.1f%%"
    )           

    plt.title("Expenses by Category")

    os.makedirs("static", exist_ok=True)

    plt.savefig("static/chart.png")
    plt.close()


def save_income_expense_chart(transactions):

    income = sum(
        t.amount 
        for t in transactions
        if t.type == "income"
    )  

    expense = sum(
        t.amount 
        for t in transactions
        if t.type == "expense"
    ) 

    plt.figure(figsize=(6,4))

    plt.bar(
        ["Income","Expense"],
        [income, expense]
    ) 

    plt.title("Income vs Expense")

    os.makedirs("static", exist_ok=True)

    plt.savefig("static/income_expense.png")

    plt.close()