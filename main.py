import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars() 
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            scoreboard.stop()
            game_is_on = False


    if player.ycor() > 300:
        player.goto(*(0, -280))
        scoreboard.add_point()

    
screen.exitonclick()
    
