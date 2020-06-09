# Expense-Tracker
An expense tracker using a simple API.

Requirements:
Python
docopt
tabulate
sqlite3 


To install the packages use the command:
pip install <package_name>


Run through terminal commands listed below:

Usage for command:

Initialize a user profile:
total_spent_driver.py init
 
Check the view of the items in the database
total_spent_driver.py view [<view_category>]

Add an expense to the database, entering a message is optional
total_spent_driver.py <amount> <category> [<message>]
