first = input("Please enter your first name: ")
last = input("Please enter your last name: ")

# output = ("Your name is " + last.capitalize() + ", " + first.capitalize() + " " + last.capitalize())
# output = "Your name is {1}, {0} {1}.".format(first.capitalize(), last.capitalize())
# output = "Your name is {}, {} {}.".format(last.capitalize(), first.capitalize(), last.capitalize())
output = f'Your name is {last.capitalize()}, {first.capitalize()} {last.capitalize()}.'

print(output)