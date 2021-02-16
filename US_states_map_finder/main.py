from turtle import Turtle, Screen
import pandas as pd

#Screen setup
screen = Screen()
screen.bgpic('/blank_states_img.gif')
screen.setup(725, 491)
screen.title("US States Guess Game")

#turtle setup
turtle = Turtle()
turtle.hideturtle()
turtle.penup()
#csv data cleaning and extracting
data = pd.read_csv('50_states.csv')
states = data["state"].to_list()
x = data.x.to_list()
y = data.y.to_list()

score = 0



while score != 50:
    answer = screen.textinput(title=f"Guess the state {score} / 50", prompt="What's another state's name?")
    if answer in states:
        state_data = data[data.state == answer]
        turtle.goto(int(state_data.x),int (state_data.y))
        turtle.write(answer)
        score += 1






#get cooridinates of each state on the map
# def get_mouse_click_coor(x, y):
#     print(x, y)
# screen.onscreenclick(get_mouse_click_coor)

screen.mainloop()

















