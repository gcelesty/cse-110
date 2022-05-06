import math
user = int(input("\nHow many columns and rows do you want in your multiplication table? "))

max = user * user
digits = int(math.log10(max)) + 1


multiply = 1
first = 1
copy = user + 1
for i in range(1, copy, multiply): # goes up and down first line
    for i in range(first, copy, multiply): # goes left and right every line
        print(f"{i:{digits}}", end=" ")
    print()
    copy = user + copy
    first = first + 1
    multiply = multiply + 1