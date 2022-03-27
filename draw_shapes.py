import random
from turtle import Turtle,Screen
abhi = Turtle()
num_sides = 2
count = 10

while count > 0 and num_sides < 10:
    num_sides += 1
    color = "blue"
    count -= 1
    angle = 360/num_sides
    colors = ["red", "green", "orange", "blue", "yellow", "pink","black","magenta"]
    abhi.color(random.choice(colors))
    for n in range(num_sides):
        abhi.forward(100)
        abhi.right(angle)


























screen = Screen()
screen.exitonclick()