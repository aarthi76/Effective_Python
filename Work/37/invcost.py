import sys
import csv
from report import read_inventory
# F-Strings
# print(f'{sys.argv = }')

def inventory_cost(filename):
    '''
    Find the total cost of inventory.csv
    '''
    total_cost = 0.0
    inv = read_inventory(filename)
    for prod in inv:
        total_cost += prod['quant'] * prod['price']
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "..\Data\inventory.csv"

cost = inventory_cost(filename)
print("Total Cost: ", cost)