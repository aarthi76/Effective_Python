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

total_cost = 0.0
inventory = read_inventory('../Data/inventory.csv')
for prd in inventory:
    total_cost += prd['quant'] * prd['price']

latest_prices = read_prices('../Data/prices.csv')
latest_cost = 0.0
for prd in inventory:
    latest_cost += prd['quant'] * latest_prices[prd['name']]

print(f'Total gain/loss: {latest_cost - total_cost}')