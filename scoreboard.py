from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT_SCORE = "left"
ALIGNMENT_GO = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-290, 260)
        self.hideturtle()
        self.color("black")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT_SCORE, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT_GO, font=FONT)

    def up_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
