from pickle import FALSE


print("\nPlease respond the following questions with numbers from 1-10: \n")

loan = int(input("How large is the loan? "))
credit = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down = int(input("How large is your down payment? "))

should_loan = True

if loan >= 5:
    if credit >= 7 and income >= 7:
        should_loan = True
    elif credit >= 7 or income >= 7:
        if down >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False

else:
    if loan <= 4:
        if credit < 4:
            should_loan = False
        elif credit >= 4:
            if income >= 7 or down >= 7:
                should_loan = True
            elif income >= 4 and down >= 4:
                should_loan = True
            else:
                should_loan = False

if should_loan:
    print("\nThe decision is yes. This is a good loan.\n")
else:
    print("\nThe decision is no. You should not loan this money.\n")
        

    
