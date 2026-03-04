import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.listen()
tim = Player()
scoreboard = Scoreboard()
cars = []
is_on = True
car_manager = CarManager()
screen.onkey(tim.move,"Up")
while is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_turtle()
    car_manager.move_turtles()
    # Detects that the turtle has successfully reached the other end.
    if tim.ycor() >= 290:
            scoreboard.add_score()
            tim.goto(0,-280)
            car_manager.increment()
    # Detects the collision.
    for i in car_manager.turtles:
          if tim.distance(i)<20:
                is_on = False
                scoreboard.end()
screen.exitonclick()