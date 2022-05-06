# Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
# T = temperature in F, V = wind speed mph, V^0.16 means V to the power of 0.16.....in python use **


def windspeed_calculation():
    # loop to have the wind speend go from 5 to 60 in increments of 5 then stop
    for x in range (0, 60, 5):
        x += 5
        # calculates wind chill if choice is "c" with the added line of adjusting the temp
        if choice == "C":
            temp_new = (temp * (9 / 5)) + 32
            wind_chill = 35.74 + (0.6215 * temp_new) - 35.75 * (x ** 0.16) + (0.4275 * temp_new * (x ** 0.16))
            print (f"At temperature {temp_new}F, wind speed at {x} mph, the windchill is: {wind_chill:.2f}F")
        # calculates wind chill if choice is "f"
        elif choice == "F":
            wind_chill = 35.74 + (0.6215 * temp) - (35.75 * (x ** 0.16)) + (0.4275 * temp * (x ** 0.16))
            print (f"At temperature {temp}F, and wind speed at {x} mph, the windchill is: {wind_chill:.2f}F. ")
    
temp = float(input("\nWhat is the temperature? "))
choice = input("Fahrenheit or Celsius (F/C)? ").upper() # the .upper() at end of code reduces the lines and amount of code throughout

# DONT print(windspeed_calculation()) BC IT WILL SHOW "None" AT END OF CODE
# since there is already a print statment in the function above there is no need to here, just call it
windspeed_calculation()
