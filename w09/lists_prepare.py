# # clients = ["Emily", "Mikey", "Tete"]



# clients = []
# # clients.append("Emily")
# # clients.append("Jackie")
# # clients.append("Nickie")

# new_client = ""
# print()
# while new_client != "quit":
#     new_client = input("What is the name of a client (type 'quit' to stop)? ")
#     clients.append(new_client)


# for client in clients:
#     print(client)

# print()




tips = [12.25, 13.95, 8.50]

running_total = 0
for tip_amount in tips:
    # running_total = running_total + tip_amount
    running_total += tip_amount 
    # SAMRE THING, JUST SHORTHAND

print(f"\nThe total is: {running_total:.2f}\n")

# NEVER CREATE A VARIABLE NAMED AS 'list' BC IT WILL ACCEPTED 
# AS SOMETHING ELSE!!!!!!!!!!!!!!