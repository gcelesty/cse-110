print("Please enter the following information:\n")

# all the variables for the badge
first = input("First name: ")
last = input("Last name: ")
email = input("Email address: ")
phone = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID Number: ")

# additional stuff
hair = input("Hair color: ")
eyes = input("Eye color: ")
month = input("Starting Month: ")
training = input("Completed additional training? (Yes/No): ")

# the id card title
print("\nThe ID Card is: \n----------------------------------------")
# 1: LAST, First
print(last.upper() + ", " + first.capitalize())
# 2: job title with every word capitalized
print(job_title.title())
# 3: ID: number
print("ID: " + id_number)

# 4: email in all lowercase
print("\n" + email.lower())
# 5: phone number written as (xxx) xxx-xxxx
print("({}{}{}) {}{}{}-{}{}{}{}".format(*phone))
# the * unpacks the 10 digits into the {}

# 5: these are other ways to code a phone number
# print("({}) {}-{}".format(phone_number[:3],phone_number[3:6],phone_number[6:]))
# print(f'({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}')

# 6: hair color and then eye color with both capitalized
# on the SAME LINE (\t)
print(f"\nHair: {hair.capitalize()}\tEyes: {eyes.capitalize()}")
# 7: training month and completed or not
print(f"Month: {month.capitalize()}\tTraining: {training.capitalize()}")

print("----------------------------------------")
