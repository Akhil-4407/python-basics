from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore =int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score} High Score: {self.highscore}",False,align="center",font=("Arial",24,"normal"))
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt","w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
    def score_check(self):
        self.score += 1
        self.update_scoreboard()