from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:

    def __init__(self):
        self.players = []
        player = Turtle(shape="turtle")
        player.penup()
        player.setpos(STARTING_POSITION)
        player.color("black")
        player.setheading(90)
        self.players.append(player)
        self.p1 = self.players[0]

    def move(self):
        self.p1.forward(MOVE_DISTANCE)

    def finish_line(self):
        if self.p1.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def reset(self):
        self.p1.goto(STARTING_POSITION)
