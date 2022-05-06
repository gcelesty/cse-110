# getting the info
child_meal = float(input("\nWhat is the price of a child's meal? $"))
adult_meal = float(input("What is the price of an adult's meal? $"))
child_num = int(input("How many children are there? "))
adult_num = int(input("How many adults are there? "))
drink = float(input("What is the price of a drink? $")) # EXTRA
drink_num = int(input("How many drinks are you getting? ")) # EXTRA
app = float(input("What is the price of an appetizer? $")) # EXTRA
app_num = int(input("How many appetizers are you getting? ")) # EXTRA
rate = float(input("What is the sales tax rate? "))
tip_percent = float(input("How much would you like to tip (percentage)? ")) # EXTRA


# doing the math
sub = (child_meal * child_num) + (adult_meal * adult_num) + (drink * drink_num) + (app * app_num)
print(f"\nSubtotal: ${sub:.2f}")
tip = sub * tip_percent / 100 # EXTRA
print(f"Tip: ${tip:.2f}") # EXTRA
tax = sub * rate / 100
print(f"Sales Tax: ${tax:.2f}")
total = sub + tax + tip
print(f"Total: ${total:.2f}")

# if else statement to give the customer a comment of how much they spent
too_much = 99
if total > too_much:
    print("You should've used a coupon!")
else:
    print("Good job at saving!")


# payment amount and then change
amount = float(input("\nWhat is the payment amount? $"))
change = amount - total
print(f"Change: ${change:.2f}\n")