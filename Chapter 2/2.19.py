# (Financial application: calculate future investment value) Write a program that
# reads in an investment amount, the annual interest rate, and the number of years,
# and displays the future investment value using the following formula:
# For example, if you enter the amount 1000, an annual interest rate of 4.25%,
# and the number of years as 1, the future investment value is 1043.33. Here is a
# sample run:
# futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate)numberOfMonths
# Enter investment amount:1000
# Enter annual interest rate:4.25
# Enter number of years:1
# Accumulated value is 1043.33
investmentAmount = eval(input("Enter investment amount: "))
annualInterestRate = eval(input("Enter annual interest rate: "))
numberOfYears = eval(input("Enter number of years: "))

monthlyInterestRate = annualInterestRate / 1200
numberOfMonths = numberOfYears * 12

futureInvestmentValue = investmentAmount * \
    (1 + monthlyInterestRate) ** numberOfMonths

print("Accumulated value is", int(futureInvestmentValue * 100) / 100)
