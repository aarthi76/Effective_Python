import sys
import csv
# F-Strings
# print(f'{sys.argv = }')

def inventory_cost(filename):
    '''
    Find the total cost of inventory.csv
    '''
    total_cost = 0.0
    with open(filename) as file:
        data = csv.reader(file)
        # ignore the first line
        headers = next(file)
    
        for row in data:
            try:
                quant = int(row[1])
                price = float(row[2])
            except ValueError as e:
                print(f"Bad row: {row}")
                continue

            total_cost += quant * price
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "..\Data\inventory.csv"

cost = inventory_cost(filename)
print("Total Cost: ", cost)