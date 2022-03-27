import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
num_of_cars = 10
p = Player()
count = 0
screen.listen()
scoreboard = Scoreboard()
scoreboard.level()
sleep_time = 0.1



screen.onkey(p.move, "Up")
cars = []

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    if count % 5 == 0:
        c = CarManager()
        cars.append(c)
    for car in cars:
        car.move()
        if car.distance(p) < 20:
            scoreboard.end_game()
            game_is_on = False
    if p.ycor() >= 280:
        p.setposition(0, -280)
        sleep_time *= 0.6
        scoreboard.level_up()
        scoreboard.level()

    count += 1



    # for c in cars:
    #     c.move(random.randint(0,10))
    #     if p.distance(c) <= 20:
    #         scoreBord = Scoreboard()
    #         game_is_on = False

screen.exitonclick()
