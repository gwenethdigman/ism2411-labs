# Reflection Questions:
# 1. The first bug I was able to spot immediately was the syntax error where it was missing a colon. The traceback statement did help me identify where the syntax error was exactly. I did have to to look at it for a couple seconds and then I was able to realize what it was missing. 
# 2. The "apply_discount(price, tier)" function says to apply a certian discount depending on what the price and tier  is. For example, if the tier is "gold", it applies a 15% discount. I think that just looking at this line of code you could easily figure out the goal of what it is trying to achieve, because the function name and parameters clearly indicate its purpose.
# 3. I did use AI on this lab but not to just get the assignment done but rather gather a deeper understanding of how to complete each of the different tasks and the fundamentals of why we do certain things in programming. 

# Exercise 1: calculate_tax

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax (100, 0.07)
tax2 = calculate_tax (250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") # 20.00


# Exercise 2: apply_discount

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85  # Apply 15% discount
    elif tier == "silver":
        return price * 0.90  # Apply 10% discount
    elif tier == "bronze":
        return price * 0.95  
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]
        
for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")
# Exercise 3: Compose them

# Write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${after_tax:.2f}")

# Refactor into function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

result = final_price(200, "gold", 0.07)
print(f'final_price(200, "gold", 0.07) = ${result:.2f}')

# Exercise 4: Loop + function


orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# Exercise 5: Debug First, Then Ask
# 1. The first bug I immediately was able to indentify is one that VS code immediately flagged was a problem. The issue was that after the for line of code it was missing a colon at the end. This is called a syntax error.
# 2. This second error I found was a IndexError because in line 15 it had an = sign but that is not correct because in python index starts from 0 and the i is then being compared with an item that doesn't exist. 
# 3. The third was a logic error in line 6 it just said = but needed to be += to calculate the accumulated total sales.
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale # Accumulate the total sales
print(f"Total: ${total}")

count = 0
for sale in sales: # Fix the syntax error
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): # Fix the condition to avoid index error
    print(sales[i])
    i += 1


# Exercise 6: Scope experiment


x = 100 #apple


def double_it():
    x = 999 # local another apple (not the same apple as above)
    return x * 2

print(x)    # 100
print(double_it()) # 1998
print(x)    # 100
