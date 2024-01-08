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
    
        for n, row in enumerate(data, start=1):
            record = dict(zip(headers, row))
            try:
                quant = int(record['quant'])
                price = float(record['price'])
            except ValueError as e:
                print(f"Row {n}: Couldn't convert: {row}")
                continue

            total_cost += quant * price
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "..\Data\inventory.csv"

cost = inventory_cost(filename)
print("Total Cost: ", cost)