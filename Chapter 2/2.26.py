# (Turtle: draw a circle) Write a program that prompts the user to enter the
# center and radius of a circle, and then displays the circle and its area, as shown
# in Figure 2.5.
import turtle

x, y, radius = eval(input("Enter the center x, y, and radius: "))

area = 3.1415 * radius * radius

turtle.penup()
turtle.goto(x, y - radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(x, y)
turtle.write(int(area * 100) / 100)
turtle.hideturtle()

turtle.done()