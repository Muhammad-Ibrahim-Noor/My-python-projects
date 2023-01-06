import turtle
import pandas as pd

file = pd.read_csv("50_states.csv")

states = file['state'].tolist()
screen = turtle.Screen()
screen.title('US states game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()
t.penup()
t.hideturtle()
score = 0
guessed_states = []
while score != 50:
    missing_states = []
    answer = (screen.textinput(f'Guess state? {score}/50', 'Guess the name of the state?')).title()
    location = file[file.state == answer]
    if answer in states:
        score += 1
        t.goto(int(location.x), int(location.y))
        t.write(answer)
        guessed_states.append(answer)
    elif answer == 'Exit':
        break
    elif answer != states:
        again = screen.textinput('Guess again', 'Guess again')

screen.exitonclick()
