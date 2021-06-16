from turtle import Turtle

ALIGNMENT = "center"
FONT = "Courier", 16, "normal"

# 5. Create a scoreboard
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

    def points(self):
        self.score += 1

    def current_score(self):
        self.clear()
        self.write(f"Current Score:  {self.score}", move=False, align=ALIGNMENT, font= (FONT))
        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.color("white")

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over. \nFinal Score:  {self.score}", align= ALIGNMENT, font= FONT)

    # Creating Instructions:
    def instructions(self):
        self.clear()
        self.write("Start/Continue: space \nPause: p", align="left")
        self.setposition(-280, -280)
        self.hideturtle()
        self.penup()
        self.color("white")