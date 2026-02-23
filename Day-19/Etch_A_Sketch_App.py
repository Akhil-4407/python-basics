from turtle import Turtle,Screen
tim = Turtle()
tim.speed("fastest")
screen = Screen()
screen.listen()
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_counter_clockwise():
    tim.left(10.0)
def turn_clockwise():
    tim.right(10.0)
def clear_drawing():
    tim.goto(0,0)
    tim.clear()

screen.onkey(fun=move_forward,key="w")
screen.onkey(fun=move_backward,key="s")
screen.onkey(fun=turn_counter_clockwise,key="a")
screen.onkey(fun=turn_clockwise,key="d")
screen.onkey(fun=clear_drawing,key="c")
screen.exitonclick()