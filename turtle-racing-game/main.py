import time

from turtle import  Screen
from player import Player
from cars import Cars

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
car = Cars()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    #detect the car and turtle clashing
    if car.distance(player) < 50:
        print("game over")


screen.exitonclick()