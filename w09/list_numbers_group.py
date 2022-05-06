print("\nEnter a list of numbers, type 0 when finished.")

numbers = []
number = -1
while number != 0:
    number = int(input("Enter number: "))
    if number != 0:
        numbers.append(number)

sum = 0
count = 0
for number in numbers:
    sum += number
    count += 1
print(f"The sum is: {sum}")

average = sum / count
print(f"The average is: {average}")

print("The largest number is:", max(numbers))
print("The smallest positive number is:", min([number for number in numbers if number > 0]))

numbers.sort()
print("The sorted list is:")
for number in numbers:
    print(number)
print()
