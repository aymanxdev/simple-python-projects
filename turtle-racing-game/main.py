import time

from turtle import  Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard

### Screen initialaiseation ###
screen = Screen()
screen.setup(600,600)
screen.tracer(0)
screen.title("Turtle Racing Game")
screen.listen()
### Screen Turle ###
player = Player()
screen.onkey(player.move_up, "Up")

###Car manager ###
car_manager = Cars()

scoreboard = Scoreboard()

scoreboard.update_score()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for moving_car in car_manager.all_cars:
        if moving_car.distance(player) < 20:
          game_is_on = False
          scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.add_point()



screen.exitonclick()