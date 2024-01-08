'''
    Calculate Gain/Loss in Inventory
'''
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
                name = row[0]
                quant = int(row[1])
                price = float(row[2])
                inv.append((name, quant, price))
            except ValueError as e:
                print(f"Bad row: {row}")
                continue
        for name,quant,price in inv:
            total += quant * price
    return total 

inv = read_inventory('../Data/inventory.csv')
pprint(inv)