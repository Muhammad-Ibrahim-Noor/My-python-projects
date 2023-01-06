import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Traffic Turtle.exe")
screen.setup(width=600, height=600)
screen.tracer(0)
our_player = Player()
score_board = Scoreboard()
screen.listen()
screen.onkeypress(our_player.go_up, "Up")
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car()
    car_manager.move_car()
    # Detect collision with car
    for each_car in car_manager.all_cars:
        if each_car.distance(our_player) < 20:
            game_is_on = False
            score_board.game_over()
    if our_player.reach_finish_line():
        our_player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()

screen.exitonclick()
