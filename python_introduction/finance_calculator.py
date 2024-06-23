monthlyIncome = int(input("Enter your monthly income:"))
monthlyExpenses = int(input("Enter your total monthly expenses:"))
monthlySavings = monthlyIncome - monthlyExpenses
projectedSaving = monthlySavings * 12 + (monthlySavings * 12 * 0.05)
print( "Your projected saving after one year,with interest,is:",projectedSaving)