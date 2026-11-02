#inventory.py
# Author: [Gweneth Digman]
# Module 10 Lab: Inventory List Manager

# Reflection Questions:
# 1. What suprised me the most is that numbers are not allowed or usually in lists
#  and also the order that the lists go in. Also, how much capitals affect the list order.
# 2. A business situation where this would be useful would be at my administrative assistant
# job where I am in charge of insuring that all of the materials and inventory needed
# for an event are accounted for, this would help to quickly organize that information.

print("---Exercise 1: Build the list ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("---Exercise 2: Index Practice---")
print(inventory[0]) # first item
print(inventory[-1]) # last item
middle = len(inventory) // 2
print(inventory[middle]) # middle item



print("---Exercise 3: Slicing Practice---")
print(inventory[0:3]) # first three items
print(inventory[-2:]) # last two items
print(inventory[::2]) # every second item

print("---Exercise 4: Modifying the list---")
inventory.append("envelope") 

print(inventory)
inventory.remove('tape')
print(inventory)
inventory.sort()
print(inventory)

print("Exercise 5: Tuple Comparison")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")

print(coords)

print("Exercise 6: Average List of sales---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")


## Exam question explanation
best = sales[0]
worst = sales[0]
# [100, 250, 75, 480, 200]
for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best (manual): {best}")
print(f"Worst (manual): {worst}")

print("--- Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * .9, 2)) # 10% discount

print("Original prices:", prices)
print("Discounts:", discount)

print("--- Exercise 8: Filter above a threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales)}")
# Reflection: What supprised me most about how lists work in python: 
# Two to three sentences
#
# Reflection: A business situation where a python list would have saved me time
# Two to three sentences
#