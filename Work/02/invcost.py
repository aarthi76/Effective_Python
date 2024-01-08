import csv
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
            quant = int(row[1])
            price = float(row[2])
            total_cost += quant * price
    return total_cost

cost = inventory_cost("..\Data\inventory.csv")
print("Total Cost: ", cost)