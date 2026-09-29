# (Geometry: area of a triangle) Write a program that prompts the user to enter the
# three points (x1, y1), (x2, y2), and (x3, y3) of a triangle and displays its area.
# The formula for computing the area of a triangle is
# Here is a sample run:
# area = 2s(s - side1)(s - side2)(s - side3)
# s = (side1 + side2 + side3) / 2
# Enter three points for a triangle: 1.5, -3.4, 4.6, 5, 9.5, -3.4
# The area of the triangle is 33.6
# *2.11 (Financial application: investment amount) Suppose you want to deposit a
# certain amount of money into a savings account with a fixed annual interest rate.
# What amount do you need to deposit in order to have $5,000 in the account after
# three years? The initial deposit amount can be obtained using the following
# formula:
# Write a program that prompts the user to enter final account value, annual interest
# rate in percent, and the number of years, and displays the initial deposit amount.
# Here is a sample run:
# initialDepositAmount = finalAccountValue
# (1 + monthlyInterestRate)numberOfMonths
x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle: "))

side1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
side2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
side3 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

print("The area of the triangle is", int(area * 1000 + 0.5) / 1000)