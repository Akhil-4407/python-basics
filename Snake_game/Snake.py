from turtle import Turtle
L = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for i in L:
            self.add_segment(i)
    def add_segment(self,p):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(p)
        self.segments.append(tim)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            x_pos = self.segments[i-1].xcor()
            y_pos = self.segments[i-1].ycor()
            self.segments[i].goto(x_pos,y_pos)
        self.head.forward(20)
    def up(self):
        if self.head.heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.segments[0].setheading(270)
    def right(self):
        if self.head.heading() != 180:
            self.segments[0].setheading(0)
    def left(self):
        if self.head.heading() != 0:
            self.segments[0].setheading(180)
    
