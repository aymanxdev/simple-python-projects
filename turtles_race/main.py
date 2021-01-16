
from turtle import Turtle, Screen

import random
race_on = False
screen = Screen()
tim = Turtle()
# tim.shape("turtle")
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your guess", prompt="Which turtle will win the race? Enter a colour")
colours = ["purple", "yellow", "red", "blue", "green", "orange"]

y_corns =[-70, -40, -10, 20, 50, 80]
all_turtles = []

for n_turtle in range(0, 6):
    tim = Turtle(shape= "turtle")
    tim.penup()
    tim.color(colours[n_turtle])
    tim.goto(x=-230, y=y_corns[n_turtle])
    all_turtles.append(tim)

if user_input:
    race_on= True
while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You have won! The {winning_color} turtle is the winner ")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner ")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
