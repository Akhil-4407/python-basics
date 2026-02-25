from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.write("Score "+ str(self.score),False,align="center",font=("Arial",24,"normal"))
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over.",False,align="center",font=("Arial",28,"normal"))
    def score_check(self):
        self.score += 1
        self.clear()
        self.write("Score "+str(self.score),move=False,align="center",font=("Arial",24,"normal"))
    

        