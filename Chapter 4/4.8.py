# (Sort three integers) Write a program that prompts the user to enter three integers
# and displays them in increasing order

number1, number2, number3 = eval(input("Enter three integers: "))

if number1 > number2:
    temporary = number1
    number1 = number2
    number2 = temporary

if number2 > number3:
    temporary = number2
    number2 = number3
    number3 = temporary

if number1 > number2:
    temporary = number1
    number1 = number2
    number2 = temporary

print("The integers in increasing order are", number1, number2, number3)