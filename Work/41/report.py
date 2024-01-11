'''
    Calculate Gain/Loss in inventory
'''

import csv
from fileparse import parse_csv
from product import Product
from tableformat import create_formatter

def read_inventory(filename):
    with open(filename) as FH:
        invdicts = parse_csv(FH,
                        select=['name', 'quant', 'price'],
                        types=[str, int, float]
                       )
        inv = [ Product(pr['name'], pr['quant'], pr['price']) 
                 for pr in invdicts 
              ] 

    return inv

def read_prices(filename):
    with open(filename) as FH:
        prices = parse_csv(FH,
                           has_headers=False,
                           types=[str, float]
                           )
        prices = dict(prices)

    return prices

def make_report(inventory, prices):
    report = list()
    for prd in inventory:
        name    = prd.name
        quant   = prd.quant
        latest  = prices[name]
        change  = latest - prd.price
        one_row = (name, quant, latest, change)
        report.append(one_row)
        
    return report

def print_report(report, formatter):
    headers = ('Name', 'Quantity', 'Price', 'Change')
    formatter.headings(headers)

    for name, quant, price, change in report:
        rowdata = [name, str(quant), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def inventory_report(inventory_filename, prices_filename, fmt='txt'):
    inventory = read_inventory(inventory_filename)
    prices = read_prices(prices_filename)
    report = make_report(inventory, prices)

    formatter = create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    if len(args) == 4:
        inv_file = args[1]
        prc_file = args[2]
        fmt = args[3]
        inventory_report(inv_file, prc_file, fmt)
    else:
        inventory_report('../Data/inventory.csv', '../Data/prices.csv')

#print("From report", __name__)
if __name__ == "__main__":
    import sys
    main(sys.argv)