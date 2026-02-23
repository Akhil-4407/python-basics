from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet: ", prompt="Which turtle will win the race? Enter a color: ").lower().strip()
y_pos = [30,-30,0,60,-60]
colors = ["red","yellow","blue","green","orange"]
l = []
for i in range(0,5):
    tim= Turtle("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-230,y_pos[i])
    l.append(tim)
is_on = True
while is_on:
    for i in l:
        random_choice = random.randint(0,10)
        i.forward(random_choice)
        if i.xcor()>230:
            winning_color = i.pencolor()
            is_on = False
            if winning_color == user_bet:
                print("You've won and the color was " + winning_color)
            else:
                print("You've lost and the color was " + winning_color)

        


screen.exitonclick()