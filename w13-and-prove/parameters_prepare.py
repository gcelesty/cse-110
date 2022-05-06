# PRINT TIME REPEATED CODE
# from datetime import datetime

# # Function to print current date and time
# def print_time(task_name):
#     print(task_name)
#     print(datetime.now())
#     print()

# #  print timestamps to see how long sections of code take to run
# first_name = "Tete"
# print_time("printed first name")

# for x in range(0,10):
#     print(x)
# print_time("completed for loop")





# GET INITIALS
# will return the first initial of a name
# def get_initial(name):
#     initial = name[0:1].upper()
#     return initial
# first = input("Enter your first name: ")
# middle = input("Enter your middle name: ")
# last = input("Enter your last name: ")

# print("Your initials are: " + get_initial(first) + get_initial(middle) + get_initial(last))



# will return the first initial of a name, the true assumes that 
# if false if not stated than the if statement will run true
def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial
first = input("Enter your first name: ")
middle = input("Enter your middle name: ")
last = input("Enter your last name: ")

print("Your initials are: " + get_initial(first, False) + get_initial(middle) + get_initial(last, False))