from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.score = 0
        self.color("light green")
        self.penup()
        self.goto(-10, 270)
        self.pendown()
        self.ht()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def score_track(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


