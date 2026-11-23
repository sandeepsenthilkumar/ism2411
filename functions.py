"""
SELF-ASSESSMENT ANSWERS

Question 1: I located the first bug – total = sale – from the print statement. I printed the result of what total was after the loop (or after being incremented inside it) and I received 90, not 715, which told me something wasn't right. Then I spent some time looking at the code and found that I was replacing total, instead of appending to it. I could see at once that something was wrong when I was trying to use the program as it didn't contain a colon and gave me an error on start up.

Question 2: When applying a discount, the input is an object called price (a number such as 200), and another called tier (a string such as "gold", "silver", "bronze" or "none"). Prints the discounted price. If tier is "gold" it returns 85% of the price. It will return 90% if it is "silver. If it is "bronze", it will return 95%. It will return the full price if it's something else. One of my colleagues might be able to use it without bothering to read the code, only be told they should be using those tier names and it will return a price discounted tier.

Claude AI Information: "Claude was used to its Explainer mode to learn what the IndexError traceback indicates. I am not calling for any code changes. Print statements and rubber ducking were used to find the bugs.
"""

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")

# --- Exercise 3 ---
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${final_price(200, 'gold', 0.07):.2f}")
print(f"final_price(200, 'gold', 0.07) = ${final_price(200, 'gold', 0.07):.2f}")

# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# --- Exercise 5: Fixed broken_sales.py ---
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# --- Exercise 6 ---
x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)

print("The variable x inside double_it() is local. It only exists during the function call. The global x is never changed. They are two different variables with the same name.")