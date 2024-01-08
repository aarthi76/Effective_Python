import csv
from pprint import pprint
def read_inventory(filename):
    with open(filename) as file:
        data = csv.reader(file)
        # ignore the first line
        headers = next(file)
        inv = []
        total = 0.0
        for row in data:
            try:
                inv.append({"name" : row[0], 
                            "quant" : int(row[1]), 
                            "price" : float(row[2])
                            })
            except ValueError as e:
                print(f"Bad row: {row}")
                continue
    return inv 

def read_prices(filename):
    prices = dict()
    with open(filename) as file:
        data = csv.reader(file)
        for row in data:
            try:
                prices[ row[0] ] = float(row[1])
            except IndexError as e:
                continue
    return prices

def make_report(inventory, prices):
    report = list()
    for prd in inventory:
        name = prd['name']
        quant = prd['quant']
        latest = prices[name]
        change = latest - prd['price']
        price = f'\u20B9{latest:.2f}'
        report.append((name, quant, price, change))
    
    return report

inventory = read_inventory('../Data/inventory.csv')
prices = read_prices('../Data/prices.csv')
report = make_report(inventory, prices)

headers = ('Name', 'Quantity', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
dashes = tuple(['-' * 10] * 4)
print('%10s %10s %10s %10s' % dashes)
for r in report:
    print('%10s %10d %10s %10.2f' % r)