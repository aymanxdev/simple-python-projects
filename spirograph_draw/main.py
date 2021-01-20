from turtle import Turtle, Screen
import random
import turtle as t
tim = Turtle()
# colours =["light sky blue", "dark slate blue", "medium spring green", "tomato", "gold", "pink", "midnight blue"]
t.colormode(255)
directions = [0, 90, 180, 270]

tim.speed("fastest")


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

def draw_spirograph(sizee_of_gap):
    for _ in range(int(360 / sizee_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + sizee_of_gap)

draw_spirograph(10)






# def draw_shape(num_sides):
#     angle = 360 /num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range (3, 11):
#     tim.begin_fill()
#     tim.color(random.choice(colours))
#     tim.fillcolor(random.choice(colours))
#     draw_shape(shape_side_n)
#     for _ in range (3,11):
#         tim.end_fill()








screen = Screen()
screen.exitonclick()