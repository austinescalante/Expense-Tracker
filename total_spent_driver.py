usage = '''
Expense Tracker CLI.
Usage:
  total_spent_driver.py init
  total_spent_driver.py view [<view_category>]
  total_spent_driver.py <amount> <category> [<message>]
'''

from docopt import docopt
from total_spent import *
from tabulate import tabulate

args = docopt(usage)

if args['init']:
    init()
    print("User Profile Created")

if args['view']:
    category = args['<view_category>']
    amount, results = view(category)
    print("Total expense: ", amount)
    print(tabulate(results))

if args['<amount>']:
    try:
        amount = float(args['<amount>'])
        log(amount, args['<category>'], args['<message>'])
    except:
        print(usage)