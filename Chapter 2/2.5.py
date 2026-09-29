# (Financial application: calculate tips) Write a program that reads the subtotal and
# the gratuity rate and computes the gratuity and total. For example, if the user
# enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
# as the gratuity and 11.5 as the total.

subtotal = eval(input("Enter the subtotal: "))
gratuityrate = eval(input("Enter the gratuity rate: "))

gratuity = subtotal * (gratuityrate/100)
total = subtotal + gratuity

print(f"The gratuity is {gratuity} and the total is {total}")