'''
    Calculate Gain/Loss in inventory
'''

import csv
from fileparse import parse_csv
from product import Product

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

def print_report(report):
    headers = ('Name', 'Quantity', 'Price', 'Change')
    dashes = tuple(['-' * 10] * 4)

    print("%10s %10s %10s %10s" % headers)
    print("%10s %10s %10s %10s" % dashes)
    for row in report:
        print("%10s %10d %10.2f %10.2f" % row)

def inventory_report(inventory_filename, prices_filename):
    inventory = read_inventory(inventory_filename)
    prices = read_prices(prices_filename)
    report = make_report(inventory, prices)
    print_report(report)

def main(args):
    if len(args) == 3:
        inv_file = args[1]
        prc_file = args[2]
        inventory_report(inv_file, prc_file)
    else:
        inventory_report('../Data/inventory.csv', '../Data/prices.csv')

#print("From report", __name__)
if __name__ == "__main__":
    import sys
    main(sys.argv)