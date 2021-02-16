from turtle import Turtle, Screen
import pandas as pd

#Screen setup
screen = Screen()
screen.bgpic('blank_states_img.gif')
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


guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"Guess the state {guessed_states} / 50", prompt="What's another state's name?").title()

    if answer == "Exit":
      states_list_left = [state for state in states if state not in guessed_states]
      df = pd.DataFrame(states_list_left)
      df.to_csv("states_to_learn")
      break
    if answer in states:
      guessed_states.append(answer)
      state_data = data[data.state == answer]
      turtle.goto(int(state_data.x),int (state_data.y))
      turtle.write(answer)








#get cooridinates of each state on the map
# def get_mouse_click_coor(x, y):
#     print(x, y)
# screen.onscreenclick(get_mouse_click_coor)

screen.mainloop()

















