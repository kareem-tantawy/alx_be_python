# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # This line was missing the assignment

def convert_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit: Temperature value in Fahrenheit.

    Returns:
        Temperature value in Celsius.
    """

    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit.

    Args:
        celsius: Temperature value in Celsius.

    Returns:
        Temperature value in Fahrenheit.
    """

    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


def main():
    """Prompts user for temperature, converts it, and displays the result."""

    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

            if unit not in ("C", "F"):
                raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

            if unit == "C":
                converted_temp = convert_to_fahrenheit(temperature)
                unit_symbol = "°C"
                converted_unit_symbol = "°F"
            else:
                converted_temp = convert_to_celsius(temperature)
                unit_symbol = "°F"
                converted_unit_symbol = "°C"

            print(
                f"{temperature:.2f}{unit_symbol} is {converted_temp:.2f}{converted_unit_symbol}"
            )
            break

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()