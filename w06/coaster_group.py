age_first = int(input("\nWhat is the age of the first rider? "))
height_first = float(input("What is the height of the first rider (in inches)? "))
second = input("Is there a second rider (yes/no)? ")

can_they = True

if age_first >= 12 and age_first <= 17:
    golden_first = input("Do you have a golden pass (yes/no)? ")

if second.lower() == "yes":
    age_second = int(input("What is the age of the second rider? "))
    height_second = float(input("What is the height of the second rider (in inches)? "))
    if age_second >= 12 and age_second <= 17:
        golden_second = input("Do you have a golen pass (yes/no)? ")

    if height_first < 36 or height_second < 36:
        can_they = False
    else:
        if age_first >= 18 or age_second >= 18 or golden_first.lower() == 'yes' or golden_second.lower() == 'yes':
            can_they = True
        else:
            if height_first >= 52 and height_second >= 52 and age_first >= 12 and age_second >= 12:
                can_they = True
            elif (age_first >= 16 and age_second >= 14) or (age_first >= 14 and age_second >= 16):
                can_they = True
            else:
                can_they = False
else:
    if (age_first >= 18 or golden_first.lower() == 'yes') and height_first >= 62:
        can_they = True
    else:
        can_they = False

if can_they:
    print("\nWelcome to the ride. Please be safe and have fun!\n")
else:
    print("\nSorry, you may not ride.\n")