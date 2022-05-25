from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("light green")
        self.penup()
        self.goto(-10, 270)
        self.pendown()
        self.ht()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    def score_track(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



