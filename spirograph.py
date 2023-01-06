import turtle
from turtle import Turtle, Screen
import random

pet = Turtle()
turtle.colormode(255)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_paints = (r, g, b)
    return random_paints


pet.speed('fastest')


def spirograph(nums_needed):
    for circle in range(int(360 / nums_needed)):
        pet.color(random_colors())
        pet.setheading(pet.heading() + nums_needed)
        pet.circle(100)


spirograph(1)
screen = Screen()
screen.exitonclick()
