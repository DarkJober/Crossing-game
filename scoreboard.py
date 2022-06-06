from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 240)
        self.write(f"Level: {self.score}", move=False, align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 28, 'normal'))
