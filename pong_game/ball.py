from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ymove = 10
        self.xmove = 10
        self.move_speed = 0.1
    def move(self):
        self.goto(self.xcor()+self.xmove,self.ycor()+self.ymove)
    def bounce_y(self):
        self.ymove *= -1
    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9
    def miss(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.bounce_x()
        self.bounce_y()
   