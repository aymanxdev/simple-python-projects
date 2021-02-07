from paddle import Paddle
from turtle import Screen
from ball import Ball 
from scoreboard import Scoreboard

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
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
  time.sleep(pong_ball.move_speed)
  screen.update()
  pong_ball.move()

  #detects if the ball detects the Y axis
  if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
     pong_ball.bounce_y()
  # detects if the ball detects touches the paddle
  if pong_ball.distance(r_paddle) < 50 and pong_ball.xcor() > 320  or  pong_ball.distance(l_paddle) < 50 and pong_ball.xcor() < -320:
      pong_ball.bounce_x()
  # detects if the ball goes beyond the x axis
  if pong_ball.xcor() > 380:
     pong_ball.reset_position()
     pong_ball.bounce_x()
     scoreboard.l_point()

  if pong_ball.xcor() < -380:
     pong_ball.reset_position()
     pong_ball.bounce_x()
     scoreboard.r_point()









screen.exitonclick()