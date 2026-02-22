from turtle import Turtle,Screen
import random
colors = [(46, 92, 144), (170, 13, 26), (34, 44, 62), (141, 80, 44), (228, 154, 7), (161, 57, 88), (211, 162, 101)]
tim = Turtle()
tim.shape("turtle")
screen= Screen()
screen.colormode(255)
tim.hideturtle()
tim.speed("fastest")
tim.penup()

tim.goto(-200,-200)
number_of_dots = 100
dot_size = 20
gap = 50
for i in range(1,number_of_dots+1):
    tim.dot(20,random.choice(colors))
    tim.forward(gap)
    if i% 10 == 0:
        tim.setheading(90)
        tim.forward(gap)
        tim.setheading(180)
        tim.forward(gap * 10)
        tim.setheading(0)



screen.exitonclick()