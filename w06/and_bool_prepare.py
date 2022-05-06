# if x > 5 and y > 10:
#     # This happens if both conditions are true

# if x > 5 or y > 10:
    # This happens if either one of the conditions (or both!) are true


# if x > 5 and y > 10 and word == "taco":
#     # This happens if all three conditions are true



# if (x > 5 or x < -5) and y > 10:
#     # In this case, x can either be greater than 5 or less than negative 5, and y must
#     # always be greater than 10

# if x > 5 or x < -5 and y > 10:
    # Without parentheses, the x < -5 and y > 10 conditions go together and both must be
    # true, unless x > 5, in which case the whole statement is true


# To check if x is either 5 or 6, you might be tempted to write:
# if x == 5 or 6:
#     # INCORRECT: This does not work!

# # You must write them both out:
# if x == 5 or x == 6:
#     # This is the correct way to check


# # To check if either first_name or last_name is Scott you might be tempted to write:
# if first_name or last_name == "Scott":
#     # INCORRECT: This does not work!

# # You must write them both out:
# if first_name == "Scott" or last_name == "Scott":
#     # This is the correct way to check





is_hot = True

# You can check the value of the variable directly
if is_hot:
    print("It's hot")

# It works, but is redundant (and therefore bad practice) to check if it is True:
if is_hot == True:
    print("It's hot")




is_hot = True

# Using the "not" keyword
if not is_hot:
    print("It is not hot")

# It works, but is generally avoided to check if it is false:
if is_hot == False:
    print("It is not hot")
