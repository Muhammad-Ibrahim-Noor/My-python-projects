import turtle
from turtle import Turtle, Screen
import random

colors = ['red', 'orange', 'black', 'green', 'blue', 'purple']
game_on = False
our_pets = []
for each_pet in range(len(colors)):
    pet = Turtle(shape='turtle')
    pet.color(colors[each_pet])
    pet.penup()
    y_positions = [-100, -70, -40, -10, 20, 50]
    pet.goto((-240, y_positions[each_pet]))
    our_pets.append(pet)

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="The Race", prompt="Which turtle will win?")
if user_choice:
    game_on = True
while game_on:
    for each_pet in our_pets:
        each_pet.forward(random.randint(0, 10))
        if each_pet.xcor() > 230:

            winning_color = each_pet.pencolor()
            if user_choice == winning_color:
                print(f"You won! Your little shit won")
                game_on = False
            else:
                print(f"Fuck off!! {user_choice} bastard lost")
                game_on = False

screen.exitonclick()
