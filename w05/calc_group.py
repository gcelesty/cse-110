number = float(input("\nWhat is your grade? "))
letter = "F"

if number >= 90:
    letter = "A"
elif number >= 80:
    letter = "B"
elif number >= 70:
    letter = "C"
elif number >= 60:
    letter = "D"
else:
    letter = "F"


last = number % 10

if last >= 7:
    sign = "+"
elif last < 3:
    sign = "-"
else:
    sign = ""

if number >= 93:
    sign = ""

if letter == "F":
    sign = ""

print(letter + sign)


if letter in("A", "B", "C"):
    print("Congrats you passed!! GO OUT AND PARTY!!\n")
else:
    print("Ummm...better luck next time bestie.\n")

