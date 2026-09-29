# (Reverse number) Write a program that prompts the user to enter a four-digit inte-
# ger and displays the number in reverse order. Here is a sample run:
number = eval(input("Enter an integer: "))

firstDigit = number // 1000
secondDigit = number // 100 % 10
thirdDigit = number // 10 % 10
fourthDigit = number % 10

reversedNumber = str(fourthDigit) + str(thirdDigit) + \
    str(secondDigit) + str(firstDigit)

print("The reversed number is", reversedNumber)