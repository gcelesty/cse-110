# function will make input regular, uppercase, then lowercase
def display_regular(message):
    print(message)

def display_uppercase(message):
    new_message = message.upper()
    print(new_message)

def display_lowercase(message):
    new_message = message.lower()
    print(new_message)

message = input("\nWhat is your message? ")
display_regular(message)
display_uppercase(message)
display_lowercase(message)
print()