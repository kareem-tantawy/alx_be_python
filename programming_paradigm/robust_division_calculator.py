def safe_divide(numerator, denominator):
    try:
        return numerator / denominator
    except TypeError:
        print("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print("Erro: Cannot divide by zero.")
