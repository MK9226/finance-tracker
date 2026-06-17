from flask import (
    Flask,
    render_template,
    request,
    redirect,
    Response
)

import csv
import io

from services.database_service import(
    create_table,
    insert_transaction,
    get_all_transactions,
    delete_transaction_db,
    update_transaction_db,
    search_transactions,
    clear_transactions_db
)

create_table()

from services.finance_service import (
    get_balance,
    get_income_total,
    get_expense_total,
    get_transaction_by_id,
    update_transaction)


from models.transaction import Transaction

from services.chart_generation import(
    save_expense_chart,
    save_income_expense_chart
)

app = Flask(__name__)


@app.route("/")
def index():

    search = request.args.get("search","")

    if search:
        transactions = search_transactions(search)
    else:
        transactions = get_all_transactions()  

     
    save_expense_chart(transactions)
    save_income_expense_chart(transactions)

    balance = get_balance(transactions)
    income_total = get_income_total(transactions)
    expense_total = get_expense_total(transactions)

    return render_template("index.html", 
                           transactions=transactions, 
                           balance=balance,
                           income_total=income_total,
                           expense_total = expense_total,
                           search = search)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            category = request.form["category"]
            t_type = request.form["type"]

            transaction = Transaction(amount, category, t_type)

            insert_transaction(transaction)

            return redirect("/")
        except ValueError:
            return "Invalid input"
        
    return render_template("add.html")


@app.route("/delete/<transaction_id>")
def delete(transaction_id):

    delete_transaction_db(transaction_id)

    return redirect("/")

@app.route("/clear")
def clear():

    clear_transactions_db()

    return redirect("/")


@app.route("/edit/<transaction_id>", methods=["GET","POST"])
def edit(transaction_id):

    transactions = get_all_transactions()

    transaction = get_transaction_by_id(transactions,transaction_id)

    if transaction is None:
        return "Transaction not found"
    
    if request.method == "POST":
        amount = float(request.form["amount"])

        category = request.form["category"]

        t_type = request.form["type"]

        update_transaction(
            transaction,
            amount,
            category,
            t_type
        )

        update_transaction_db(transaction)

        return redirect("/")
    
    return render_template("edit.html", transaction=transaction)


@app.route("/charts")
def charts():

    transactions = get_all_transactions()

    return render_template(
        "charts.html",
        transactions=transactions
    )


@app.route("/export")
def export():

    transactions = get_all_transactions()

    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow([
        "Date",
        "Type",
        "Category",
        "Amount"
    ])

    for t in transactions:
        writer.writerow([
            t.date,
            t.type,
            t.category,
            t.amount
        ])

    output.seek(0)

    return Response(
        output,
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=transactions.csv"
        }
    )    


if __name__ == "__main__":
    app.run(debug=True, use_reloader = False)
