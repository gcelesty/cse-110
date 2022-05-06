print("\nEnter the names and balances of bank accounts (type: 'quit' when done)")

accounts = []
account = ""
balances = []
balance = 0

while account != "quit":
    account = input("What is the name of this account? ")
    if account != "quit":
        accounts.append(account)
        balance = float(input("What is the balance? "))
        if balance != "quit":
            balances.append(balance)
print()

count = 0
print("Account Information:")
for i in range(len(accounts)):
    account = accounts[i]
    print(f"{i}. {accounts[i]} - ${balances[i]:.2f}")
    count += balances[i]
print()

sum = sum(balances)
print(f"Total: ${sum:.2f}")
average = sum / len(balances)
print(f"Average: ${average:.2f}")

highest_account = ""
highest_balance = -1
for i in range(len(accounts)):
    account = accounts[i]
    balance = balances[i]
    if balance > highest_balance:
        highest_balance = balance
        highest_account = account
print(f"Highest balance: {highest_account} - ${highest_balance:.2f}\n")

update = "yes"
while update == "yes":
    update = input("Do you want to update an account? ")
    if update == 'yes':
        account_index = int(input("What account index do you want to update? "))
        new_balance = float(input("What is the new amount? "))
        balances[account_index] = new_balance
    print("\nAccount Information:")
    for i in range(len(accounts)):
        account = accounts[i]
        print(f"{i}. {accounts[i]} - ${balances[i]:.2f}")
        count += balances[i]
    print()