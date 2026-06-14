from datetime import datetime
import uuid

class Transaction:

    def __init__(self, amount, category, t_type, date=None, id=None):
        self.id = id if id else str(uuid.uuid4())

        self.amount = amount
        self.category = category
        self.type = t_type

        self.date = (
            date 
            if date 
            else datetime.now().strftime("%d-%m-%Y")
            )

    def __str__(self):
        return(
            f"Transaction("
            f"id={self.id},"
            f"amount={self.amount},"
            f"category='{self.category}',"
            f"type='{self.type}',"
            f"date='{self.date}')"
        ) 

  