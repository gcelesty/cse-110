first = float(input("\nWhat is the first number? "))
second = float(input("What is the second number? "))

if first > second:
    print("The first number is greater")
else:
    print("The first number is not greater")

if first == second:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if second > first:
    print("The second number is greater")
else:
    print("The second number is not greater")

animal = input("\nWhat is your favorite animal? ")

if animal.lower() == "lion":
    print("That's my favorite animal too!\n")
else:
    print("That one is not my favorite.\n")