# (Financial application: payroll) Write a program that reads the following infor-
# mation and prints a payroll statement:
# Employee’s name (e.g., Smith)
# Number of hours worked in a week (e.g., 10)
# Hourly pay rate (e.g., 9.75)
# Federal tax withholding rate (e.g., 20%)
# State tax withholding rate (e.g., 9%)

name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked in a week: "))
payRate = eval(input("Enter hourly pay rate: "))
federalRate = eval(input("Enter federal tax withholding rate: "))
stateRate = eval(input("Enter state tax withholding rate: "))

grossPay = hours * payRate
federalWithholding = grossPay * federalRate
stateWithholding = grossPay * stateRate
totalDeduction = federalWithholding + stateWithholding
netPay = grossPay - totalDeduction

print()
print("Employee Name:", name)
print("Hours Worked:", hours)
print("Pay Rate: $" + format(payRate, ".2f"))
print("Gross Pay: $" + format(grossPay, ".2f"))
print("Deductions:")
print("  Federal Withholding (" + format(federalRate, ".1%")
      + "): $" + format(federalWithholding, ".2f"))
print("  State Withholding (" + format(stateRate, ".1%")
      + "): $" + format(stateWithholding, ".2f"))
print("  Total Deduction: $" + format(totalDeduction, ".2f"))
print("Net Pay: $" + format(netPay, ".2f"))