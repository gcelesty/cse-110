print("\nPlease enter the items of the shopping list (type: 'quit' to finish):")
item = ""
items = []

while item != 'quit':
    item = input("Item: ")
    if item != 'quit':
        items.append(item)

print("\nThe shopping list is:")
for item in items:
    print(item)
print()

print("The shopping list with indexes is:")
for i in range(len(items)):
    item = items[i]
    print(f"{i}. {item}")
print()

change = int(input("Which item would you like to change? "))
new = input("What is the new item? ")
items[change] = new

print("\nThe shopping list with indexes is:")
for i in range(len(items)):
    item = items[i]
    print(f"{i}. {item}")
print()