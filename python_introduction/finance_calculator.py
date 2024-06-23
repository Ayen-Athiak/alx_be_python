monthly_income =float(input("Enter your monthly income:"))
monthly_expenses =float(input("Enter your total monthly expenses:"))
monthly_savings = monthly_income - monthly_expenses
projected_Saving = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print( "Your projected saving after one year,with interest,is:",projected_Saving)