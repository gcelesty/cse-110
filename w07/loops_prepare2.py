number = int(input("\nPlease type a positive number: "))

while number < 0:
    print("Sorry, that is a negative number. Please try again.")
    number = int(input("Please type a positive number: "))

print(f"The number is: {number}\n")

# print("\n")
# answer = ""

# while answer.capitalize() != "Yes":
#     answer = input("May I have a piece of candy? ")

# print("Thank you. \n")