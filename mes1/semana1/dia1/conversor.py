# El programa debe:

# Pedir al usuario una temperatura en Celsius
# Convertirla a Fahrenheit
# Mostrar el resultado formateado
# Pedir distancia en kilómetros
# Convertirla a millas
# Mostrar el resultado
# ---------------------------------

print("=== TEMPERATURE CONVERTOR ===")
celsius: float = float(input("Enter a temperature in Celcius: "))
fahrenheit: float = (celsius * 9 / 5) + 32
print(f"Temperature in Celcius: {celsius:.2f}°C")
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")
print("")
print("=== KILOMETERS TO MILES ===")
kilometers: float = float(input("Enter your distance in KM: "))
miles: float = kilometers * 0.621371
print(f"Distance in KM: {kilometers}")
print(f"Distance in Miles: {miles:.2f}")
