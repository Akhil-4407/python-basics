from turtle import Turtle,Screen
FONT = ("courier",24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.check()
    def check(self):
        self.clear()
        self.goto(-280,250)
        self.write(f"Level: {self.score}",False,"left",FONT)
    def add_score(self):
        self.score += 1
        self.check()
    def end(self):
        self.goto(0,0)
        self.write("GAME OVER!",False,"center",FONT)