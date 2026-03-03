from turtle import Turtle
POSITION = [(350,0),(-350,0)]
class Paddle(Turtle):
    def __init__(self,a,b):
        super().__init__()
        self.x_cor = a
        self.y_cor = b 
        self.shape("square")
        self.setheading(90)
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=5,outline=2)
        self.goto(self.x_cor,self.y_cor)
    def up(self):
        self.setheading(90)
        self.forward(20)
    def down(self):
        self.setheading(270)
        self.forward(20)
    