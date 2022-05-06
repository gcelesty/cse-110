print("\nWelcome to the velocity calculator. Please enter the following: \n")
m = float(input("Mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

c = (1 / 2) * p * A * C
print(f"\nThe inner value of c is: {c:.3f}")
import math
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))
print(f"The velocity after 10.0 seconds is: {v:.3f} m/s\n")

# stretch 1


# stretch 2
earth = math.sqrt(m * 9.8 / c) * (1 - math.exp((-math.sqrt(m * 9.8 * c) / m) * t))
jupiter = math.sqrt(m * 24 / c) * (1 - math.exp((-math.sqrt(m * 24 * c) / m) * t))
print(f"\nThe velocity after 10.0 seconds on EARTH is : {earth:.3f} m/s")
print(f"The velocity after 10.0 seconds on JUPITER is : {jupiter:.3f} m/s\n")

# stretch 3: terminal velocity (fastest velocity)
vt = math.sqrt(m * g / c)
print(f"\nThe terminal velocity (the fastest speed) is {vt:.3f} m/s\n")
