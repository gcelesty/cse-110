print("\nWelcome to the Shopping Cart Program!\n")

action = 1
items = []
prices = []
while action >= 1:
    print("Please select one of the following:")
    print("1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit")
    action = int(input("Please enter an action: "))
    if action == 1:
        item = input("What item would you like to add? ")
        items.append(item)
        price = float(input(f"What is the price of '{item}'? "))
        quantity = int(input("What is the quantity? ")) # MAKE IT MY OWN
        price = price * quantity # MAKE IT MY OWN
        prices.append(price)
        print(f"'{item}' has been added to the cart.")
    elif action == 2:
        print("The contents of the shopping cart are:")
        for i in range(len(items)):
            item = items[i]
            price = prices[i]
            print(f"{i + 1}. {item} - ${price:.2f}")
    elif action == 3:
        remove = int(input("Which item would you like to remove? "))
        remove = remove - 1
        items.pop(remove)
        prices.pop(remove)
        print("Item removed.")
    elif action == 4:
        total = sum(prices)
        tax = float(input("What is your state tax (ex: Texas is 6.25, so enter .0625)? ")) # MAKE IT YOUR OWN
        total_tax = total * tax  # MAKE IT MY OWN
        total_sum = total_tax + total # MAKE IT MY OWN
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
        print(f"The sales tax of the items in the shopping cart is ${total_tax:.2f}") # MAKE IT MY OWN
        print(f"The final price of your shopping cart is ${total_sum:.2f}") # MAKE IT MY OWN
    elif action == 5:
        print("Thank you. Goodbye.\n")
        break
    else:
        print("ERROR: PLEASE ENTER A VALID OPTION")
    print()
