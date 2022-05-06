people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
min_age = 9999
min_name = ""

for person in people:
    person = person.split()
    name = person[0]
    age = int(person[1])
    if min_age > age:
        min_age = age
        min_name = name
print(f"The youngest person is: {min_name}")
print(f"With an age of: {min_age}")