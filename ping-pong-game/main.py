from paddle import Paddle
from turtle import Screen

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Ping-Pong Game (Table Tennis)")
screen.listen()
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()












screen.exitonclick()