import sqlite3
import os

from models.transaction import Transaction

DB_PATH = "database/finance.db"

def get_connection():

    os.makedirs("database", exist_ok=True)

    return sqlite3.connect(DB_PATH)

def create_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id TEXT PRIMARY KEY,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            type TEXT NOT NULL,
            date TEXT NOT NULL )
        """)
    
    conn.commit()
    conn.close()

def insert_transaction(transaction):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions
        VALUES (?,?,?,?,?)           
""", (
    transaction.id,
    transaction.amount,
    transaction.category,
    transaction.type,
    transaction.date
))   
    
    conn.commit()
    conn.close()

def get_all_transactions():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(""" 
        SELECT *
        FROM transactions
        ORDER BY date DESC                                
       """)    
    
    rows = cursor.fetchall()

    conn.close()

    return [
        Transaction(
            amount=row[1],
            category=row[2],
            t_type=row[3],
            date=row[4],
            id=row[0]
        )
        for row in rows
    ]


def delete_transaction_db(transaction_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
          DELETE FROM transactions
          WHERE id = ?           
        """, (transaction_id,))
    
    conn.commit()
    conn.close()

def update_transaction_db(transaction):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
          UPDATE transactions
          SET amount = ?,
              category = ?,
              type = ?
          WHERE id = ?                                 
        """, (transaction.amount,
              transaction.category,
              transaction.type,
              transaction.id))
    
    conn.commit()
    conn.close()


def clear_transactions_db():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   DELETE FROM transactions
                   """)
    
    conn.commit()
    conn.close()

def search_transactions(search_term):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
       SELECT *
       FROM transactions
       WHERE category LIKE ?
       OR type LIKE ?            
       ORDER BY date DESC                                    
    """, (f"%{search_term}%",
          f"%{search_term}%"))

    rows = cursor.fetchall()

    conn.close()

    return[
        Transaction(
            amount=row[1],
            category=row[2],
            t_type=row[3],
            date=row[4],
            id=row[0]
        )

        for row in rows
    ]
