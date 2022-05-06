friend = ""
friends = []

print()
while friend != "end":
    friend = input("Type the name of a friend: ")
    if friend != "end":
        friends.append(friend)

print("\nYour friends are: ")
for friend in friends:
    friend = friend.capitalize()
    print(friend)
print()