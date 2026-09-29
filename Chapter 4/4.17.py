# (Game: scissor, rock, paper) Write a program that plays the popular scissor-rock-
# paper game. (A scissor can cut a paper, a rock can knock a scissor, and a paper can
# wrap a rock.) The program randomly generates a number 0, 1, or 2 representing
# scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
# 2 and displays a message indicating whether the user or the computer wins, loses,
# or draws. Here are sample runs:

import random

computer = random.randint(0, 2)
user = eval(input("scissor (0), rock (1), paper (2): "))

if computer == 0:
    computerChoice = "scissor"
elif computer == 1:
    computerChoice = "rock"
else:
    computerChoice = "paper"

if user == 0:
    userChoice = "scissor"
elif user == 1:
    userChoice = "rock"
else:
    userChoice = "paper"

if computer == user:
    print("The computer is", computerChoice + ".", "You are", userChoice + " too. It is a draw.")
elif (user == 0 and computer == 2) or \
     (user == 1 and computer == 0) or \
     (user == 2 and computer == 1):
    print("The computer is", computerChoice + ".", "You are", userChoice + ". You won.")
else:
    print("The computer is", computerChoice + ".", "You are", userChoice + ". You lost.")