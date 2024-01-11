'''
    Calculate Gain/Loss in inventory
'''

import csv
from fileparse import parse_csv

def read_inventory(filename):
    inv = parse_csv(filename, select=['name', 'quant', 'price'], types=[str,int,float])
    return inv

def read_prices(filename):
    prices = dict(parse_csv(filename, has_headers=False, types=[str, float]))
    return prices

def make_report(inventory, prices):
    report = list()
    for prd in inventory:
        name    = prd['name']
        quant   = prd['quant']
        latest  = prices[name]
        change  = latest - prd['price']
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

if __name__ == "__main__" :    
    import sys
    main(sys.argv)
