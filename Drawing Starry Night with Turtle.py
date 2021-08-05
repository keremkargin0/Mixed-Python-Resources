from turtle import *
from random import randint

# Page setup
setup(1000, 800)
speed(5)
bgcolor("black")

# Function to draw one star
def star():
    color("yellow")
    begin_fill()
    for i in range(5):
        forward(10)
        right(144)
    end_fill()

# Draw multiple stars at random locations on the screen
for i in range(20):
    x = randint(-400, 400)
    y = randint(-250, 250)
    star()
    penup()
    goto(x, y)
    pendown()

# Moon - Part 1
penup()
goto(-300, 100)
pendown()
color("white")
begin_fill()
circle(50)
end_fill()

# Moon - Part 2
penup()
goto(-280, 100)
pendown()
color("black")
begin_fill()
circle(50)
end_fill()
