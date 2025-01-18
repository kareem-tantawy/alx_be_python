def safe_divide(numerator, denominator):
    try:
        return float(numerator) / float(denominator)
    except TypeError:
        print("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
               