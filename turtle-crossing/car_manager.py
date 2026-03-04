from turtle import Turtle
import random
COLORS = ["red","orange","yellow","green","blue","purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
cars = []
class CarManager(Turtle):
    def __init__(self):
        super().__init__() 
        self.turtles = []  
        self.hideturtle() 
    def create_turtle(self):
        self.num = random.randint(1,5)
        if self.num==1:
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.shapesize(stretch_wid=1,stretch_len=2)
            new_turtle.color(random.choice(COLORS))
            new_turtle.goto(300,random.randint(-250,250))
            self.turtles.append(new_turtle)
    def move_turtles(self):
        global STARTING_MOVE_DISTANCE
        for i in self.turtles:
            i.backward(STARTING_MOVE_DISTANCE)
    def increment(self):
        global STARTING_MOVE_DISTANCE, MOVE_INCREMENT
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT