import turtle,pandas
screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
is_on = True
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
print(states_list)
timmy = turtle.Turtle()
timmy.hideturtle()
timmy.penup()
x = 0
gussed = []
while is_on:
    answer = screen.textinput(title=f"States gussed {x}/50",prompt="What's another state")
    if answer.title() == "Exit":
        is_on = False
    else:
        if answer.title() in states_list:
            gussed.append(answer.title())
            x_pos = data[data.state == answer.title()].x.item()
            y_pos = data[data.state == answer.title()].y.item()
            timmy.goto(x_pos,y_pos)
            timmy.write(f"{answer}",False,"left",("Arial",8,"normal"))
            x+= 1

states_to_learn = [x for x in states_list if x not in gussed]
dic_states = {"States":states_to_learn}
new_data = pandas.DataFrame(dic_states)
new_data.to_csv("states_to_learn.csv")


"""For coordinates on the map"""
# def on_mouse_click(x,y):
#     print(x,y)
# turtle.onscreenclick(on_mouse_click)
# turtle.mainloop()
