# (Random character) Write a program that displays a random uppercase letter
# using the time.time() function.

import time

number = int(time.time() * 1000) % 26
letter = chr(65 + number)

print("The random uppercase letter is", letter)