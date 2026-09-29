# (Find future dates) Write a program that prompts the user to enter an integer for
# today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
# prompt the user to enter the number of days after today for a future day and dis-
# play the future day of the week. Here is a sample run:

today = eval(input("Enter today's day: "))
daysElapsed = eval(input(
    "Enter the number of days elapsed since today: "))

futureDay = (today + daysElapsed) % 7

if today == 0:
    todayName = "Sunday"
elif today == 1:
    todayName = "Monday"
elif today == 2:
    todayName = "Tuesday"
elif today == 3:
    todayName = "Wednesday"
elif today == 4:
    todayName = "Thursday"
elif today == 5:
    todayName = "Friday"
else:
    todayName = "Saturday"

if futureDay == 0:
    futureName = "Sunday"
elif futureDay == 1:
    futureName = "Monday"
elif futureDay == 2:
    futureName = "Tuesday"
elif futureDay == 3:
    futureName = "Wednesday"
elif futureDay == 4:
    futureName = "Thursday"
elif futureDay == 5:
    futureName = "Friday"
else:
    futureName = "Saturday"

print("Today is", todayName, "and the future day is", futureName)