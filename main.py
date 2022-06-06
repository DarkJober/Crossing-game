import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_speed)
    screen.update()
    car_manager.generate_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() == 280:
        player.finish_line()
        car_manager.increase_speed()
        scoreboard.increase_score()

screen.exitonclick()