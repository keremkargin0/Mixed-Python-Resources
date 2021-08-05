# Drawing so many stars with Turtle

import turtle

a = turtle.Turtle()
a.getscreen().bgcolor("#FDF0D5")

a.penup()
a.goto(-200,100)
a.pendown()
a.color("#331832")

a.speed(25)

def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
    for i in range(5):
        turtle.forward(size)
        star(turtle, size/3)
        turtle.left(216)
        turtle.end_fill()

star(a, 360)
turtle.done()
