# This is an Advance financial calculator to calculated Savings & projected future savings.

# finance_calculator_debug.py
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Debug prints - explicit, flushed, and labelled
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
