monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

yearly_savings = monthly_savings * (12 + 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}.")

print(f"Projected savings after one year, with nterest, is: ${int(yearly_savings)}.")