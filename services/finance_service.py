  
def get_transaction_by_id(transactions, transaction_id):
    for t in transactions:
        if t.id == transaction_id:
          return t
    
    return None
    

def update_transaction(transaction, amount, category, t_type):
    transaction.amount = amount
    transaction.category = category
    transaction.type = t_type


def get_balance(transactions):
    total = 0
    for t in transactions:
        if t.type == "income":
            total += t.amount
        else:
            total -= t.amount
    return total

def get_income_total(transactions):
    return sum(t.amount for t in transactions if t.type == "income")

def get_expense_total(transactions):
    return sum(t.amount for t in transactions if t.type == "expense")


def get_category_summary(transactions):
    summary = {}

    for t in transactions:
        if t.category not in summary: 
            summary[t.category]=0

        if t.type == "income":
            summary[t.category] += t.amount
        else:
            summary[t.category] -= t.amount

    return summary 

def filter_by_category(transactions, category):
    return [t for t in transactions if t.category.lower() == category.lower()]



                     
    