"""
Units conversor
Converts temperature (Celcius -> Fahrenheit) and distances (KM -> Miles)
"""

print("=== TEMPERATURE CONVERTOR ===")
celsius: float = float(input("Enter a temperature in Celsius: "))
fahrenheit: float = (celsius * 9 / 5) + 32
print(f"Temperature in Celsius: {celsius:.2f}°C")
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")
print("")
print("=== KILOMETERS TO MILES ===")
kilometers: float = float(input("Enter your distance in KM: "))
miles: float = kilometers * 0.621371
print(f"Distance in KM: {kilometers}")
print(f"Distance in Miles: {miles:.2f}")
