FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level_num = 1



    def level(self):
        self.clear()
        self.goto(-260, 260)
        self.write(f"level: {self.level_num}", "center", font=FONT)


    def end_game(self):
        self.setposition(0, 0)
        self.write("GAME OVER", "center", font=FONT)

    def level_up(self):
        self.level_num += 1
