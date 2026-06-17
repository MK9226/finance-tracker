Personal Finance Tracker 

A web-based personal finance management application built with Python, Flask , and SQLite. The application allows users to track income and expense, visualize spending habits, and export financial data. 

Features

Add new income and expense transactions
Edit existing transactions
Delete transactions
Search transactions by category
Store data using SQLite
Financial dashboard with:
   Total Income
   Total Expenses
   Current Balance
Expense Breakdown Chart(Pie Chart)
Income vs Expense Chart(Bar Chart)
Export transactions to CSV
Responsive user interface using Bootstrap 5


Technologies Used

Backend

Python
Flask
SQLite

Frontend

HTML5
CSS3
Bootstrap 5
Bootstrap Icons

Data Visualization

Matplotlib

Version Control

Git
GitHub


Installation

Clone the repository

git clone https://github.com/MK9226/finance-tracker.git
cd finance-tracker

Create a virtual environment

python -m venv venv

Active the virtual environment

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

Install dependencies

pip install -r requirements.txt


Running the Application

Start the Flask server:

python app.py

Open your browser and navigate to :

http://127.0.0.1:5000


Database 

This application uses SQLite database.

The database file is automatically created inside:

database/finance.db


Exporting Data

The application allows users to export all transactions into a CSV file:

transactions.csv

The CSV file contains:

Date 
Transaction Type
Category
Amount


Future Improvements

Monthly budget planner
Date filters
Sorting transactions
PDF report generation


Author

Mariam Kamalyan

GitHub: https://github.com/MK9226

