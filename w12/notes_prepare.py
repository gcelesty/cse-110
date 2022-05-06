# FINDING THE MAX OR MIN
# numbers = [42, 25, 18, 23, 85, 38, 2]
# max = numbers[0]

# for number in numbers:
#     if number > max:
#         max = number
# print(f"The largest is: {max}")




# KEEPING TRACK OF THE ITEM THAT IS THE MAX OR MIN
shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]
max_price = -1
max_product = "" # NEW

for item in shopping_cart:
    product = item[0] # NEW
    price = item[1]
    if price > max_price:
        max_price = price
        max_product = product # NEW
print(f"The maximum price is: {max_price}")
print(f"The product with the maximum price is: {max_product}")