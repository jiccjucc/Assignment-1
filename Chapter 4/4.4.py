# (Game: learn addition) Write a program that generates two integers under 100 and
# prompts the user to enter the sum of these two integers. The program then reports
# true if the answer is correct, false otherwise. The program is similar to Listing 4.1.

import random

number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

answer = eval(input("What is " + str(number1) + " + " + str(number2) + "? "))

print(number1, "+", number2, "=", answer, "is", number1 + number2 == answer)