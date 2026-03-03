from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard
screen = Screen()
screen.listen()
screen.tracer(0)
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong")
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
scoreboard = Scoreboard()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")
ball = Ball()
while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.xcor() > 320 and ball.distance(r_paddle) <50 ) or (ball.xcor() < -320 and ball.distance(l_paddle)<50):
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.miss()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.miss()
        scoreboard.r_point()
screen.exitonclick()
