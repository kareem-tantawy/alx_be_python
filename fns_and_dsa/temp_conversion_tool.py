FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9 * (fahrenheit - 32)
    return FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5 * celsius + 32
    return CELSIUS_TO_FAHRENHEIT_FACTOR

    """Enter the temperature to convert: 100
Is this temperature in Celsius or Fahrenheit? (C/F): F
100.0°F is 37.77777777777778°C
    """


temperature = float(input("Enter the temperature to convert: "))
F_or_C = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if F_or_C == "F":
    print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
else:
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
