from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.step = STARTING_MOVE_DISTANCE
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.num_of_cars = 10
        self.setposition(x=300, y=random.randint(-250, 250))

    def move(self):
        self.forward(self.step)

    def car_gen(self):
        new_c = self.new_car()
