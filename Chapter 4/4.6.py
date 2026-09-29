# (Health application: BMI ) Revise Listing 4.6, ComputeBMI.py, to let users enter
# their weight in pounds and their height in feet and inches. For example, if a person
# is 5 feet and 10 inches, you will enter 5 for feet and 10 for inches. Here is a sam-
# ple run:

weight = eval(input("Enter weight in pounds: "))
feet = eval(input("Enter feet: "))
inches = eval(input("Enter inches: "))

KPP = 0.45359237
MPI = 0.0254

totalInches = feet * 12 + inches
weightInKilograms = weight * KPP
heightInMeters = totalInches * MPI
bmi = weightInKilograms / (heightInMeters * heightInMeters)

print("BMI is", bmi)

if bmi < 18.5:
    print("You are Underweight")
elif bmi < 25:
    print("You are Normal")
elif bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")