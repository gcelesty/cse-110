max_life = -1
min_life = 9999
max_place = ""
min_place = ""
user_max_number = -1
user_min_number = 9999
user_max_place = ""
user_min_place = ""
user_max_number2 = -1
user_min_number2 = 9999
user_max_place2 = ""
user_min_place2 = ""
lifes = []
countries_life = []

user_year = int(input("\nEnter the year of interest: "))
user_country = input("Enter the country of interest: ")

with open("/Users/celestegeorge/Downloads/vs/w12/life-expectancy.csv") as data:
    for info in data:
        info = info.strip()
        details = info.split(",")

        country = details[0]
        abv = details[1]
        year = int(details[2])
        life = float(details[3])

        if life > max_life:
            max_life = life
            max_place = country
            max_year = year

        if life < min_life:
            min_life = life
            min_place = country
            min_year = year

        if year == user_year:
            lifes.append(life)
            if life > user_max_number:
                user_max_number = life
                user_max_place = country
            if life < user_min_number:
                user_min_number = life
                user_min_place = country
            average = sum(lifes) / len(lifes)
        
        # ########### THIS "IF" STATEMENT IS EXTRA ########### #
        if country.lower() == user_country.lower():
            countries_life.append(life)
            if life > user_max_number2:
                user_max_number2 = life
                user_max_place2 = country
            if life < user_min_number2:
                user_min_number2 = life
                user_min_place2 = country
            average2 = sum(lifes) / len(lifes)


print(f"\nThe overall max life expectancy is: {max_life} from {max_place} in {max_year}")
print(f"The overall min life expectancy is: {min_life} from {min_place} in {min_year}")
print(f"\nFor the year {user_year}:")
print(f"The average life expectancy across all countries was {average:.2f}")
print(f"The max life expectancy was in {user_max_place} with {user_max_number}")
print(f"The min life expectancy was in {user_min_place} with {user_min_number}\n")
# ############ BELOW IS ADDED INFORMATION ##################### #
print(f"\nFor the country {user_country.upper()}:")
print(f"The average life expectancy in {user_country.upper()} was {average2:.2f}")
print(f"The max life expectancy was in {user_max_place2} with {user_max_number2}")
print(f"The min life expectancy was in {user_min_place2} with {user_min_number2}\n")