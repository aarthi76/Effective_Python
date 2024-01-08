'''
    Find the total cost of inventory.csv
'''
# total_cost = 0.0
# file = open("../Data/inventory.csv")
# # ignore the first line
# headers = next(file)
# for line in file:
#     #print(line, end="")
#     parts = line.split(',')
#     quant = int(parts[1])
#     price = float(parts[2])
#     total_cost += quant * price
# print("Total Cost: ", total_cost)
import csv
total_cost = 0.0
with open("../Data/inventory.csv") as file:
    data = csv.reader(file)
    # ignore the first line
    headers = next(file)
    
    for row in data:
        quant = int(row[1])
        price = float(row[2])
        total_cost += quant * price
print("Total Cost: ", total_cost)