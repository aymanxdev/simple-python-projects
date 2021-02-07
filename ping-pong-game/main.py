from paddle import Paddle
from turtle import Screen
from ball import Ball 

import time

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

pong_ball = Ball()
game_is_on = True

while game_is_on:
  time.sleep(0.1)
  screen.update()
  pong_ball.move()

  if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
      pong_ball.bounce()










screen.exitonclick()