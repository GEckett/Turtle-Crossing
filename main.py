import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.title("Turtle Crossing")
screen.tracer(0)
screen.setup(width=600, height=600)

player = Player()
cars = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
loop_count = 0
while game_is_on:
    loop_count += 1
    time.sleep(0.1)
    for car in cars.cars:
        if car.distance(player.p1) < 20:
            game_is_on = False
            score_board.game_over()
    screen.update()
    if loop_count % 6 == 0:
        cars.create_cars()
    cars.move()
    if player.finish_line():
        score_board.up_score()
        player.reset()
        cars.speed_up()


screen.exitonclick()
