# (Turtle: draw the Olympic symbol ) Write a program that prompts the user to
# enter the radius of the rings and draws an Olympic symbol of five rings of the
# same size with the colors blue, black, red, yellow, and green, as shown in
# Figure 3.5c.

import turtle

radius = eval(input("Enter the radius of the rings: "))

turtle.pensize(3)

turtle.color("blue")
turtle.penup()
turtle.goto(-2.2 * radius, -0.5 * radius)
turtle.pendown()
turtle.circle(radius)

turtle.color("black")
turtle.penup()
turtle.goto(0, -0.5 * radius)
turtle.pendown()
turtle.circle(radius)

turtle.color("red")
turtle.penup()
turtle.goto(2.2 * radius, -0.5 * radius)
turtle.pendown()
turtle.circle(radius)

turtle.color("yellow")
turtle.penup()
turtle.goto(-1.1 * radius, -1.6 * radius)
turtle.pendown()
turtle.circle(radius)

turtle.color("green")
turtle.penup()
turtle.goto(1.1 * radius, -1.6 * radius)
turtle.pendown()
turtle.circle(radius)

turtle.hideturtle()
turtle.done()