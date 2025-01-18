def safe_divide(numerator, denominator):
    if numerator in [int, float] and denominator in [int, float]:
        raise TypeError("Error: Please enter numeric values only.")
    if denominator == 0:
        raise ZeroDivisionError("Erro: Cannot divide by zero.")
    return numerator / denominator
