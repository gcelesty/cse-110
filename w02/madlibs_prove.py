print("Please enter the following:\n")

adjective = input("adjective: ")
animal = input("animal: ")
verb_one = input("verb: ")
exclamation = input("exclamation: ")
verb_two = input("verb: ")
verb_three = input("verb: ")

print("\nYour story is: \n")

print(f'The other day, I was really in trouble. It all started when I saw a very \n{adjective} {animal} {verb_one} down the hallway. "{exclamation.capitalize()}!" I yelled. But all \nI could think to do was to {verb_two} over and over. Miraculously, \nthat caused it to stop, but not before it tried to {verb_three} \nright in front of my family.\n')

print("\nPlease enter the following:\n")

person = input("person in the room: ")
adj = input("adjective: ")
verb_four = input("verb: ")
body = input("part of the body: ")
number = input("number: ")
noun = input("noun: ")
adverb = input("adverb: ")
verb_five = input("verb: ")
pronoun = input("pronoun plural: ")
person_two = input("other person in the room: ")
phone = input("10 digit number (or your phone number): ")

print("\nYour love letter is:\n")

print(f"Dear {person.capitalize()},\n")
print(f"You are extremly {adj} and I {verb_four} you! I want kiss your {body} {number} \ntimes. You make my {noun} burn with desire. When I first saw you, I {adverb} \nstared at you and fell in love. Will you {verb_five} out with me? Don`t let your \nparents discourage you, {pronoun} are just jealous.\n")
print(f"Yours forever, {person_two.capitalize()}")
print("Call me ({}{}{}) {}{}{}-{}{}{}{}".format(*phone) + "\n")
