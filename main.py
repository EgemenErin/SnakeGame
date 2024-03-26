import time
from turtle import Screen

import snake
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

hania = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(hania.up, "Up")
screen.onkey(hania.down, "Down")
screen.onkey(hania.right, "Right")
screen.onkey(hania.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    hania.move()

    if hania.head.distance(food) < 15:
        hania.extend_snake()
        food.refresh()
        scoreboard.scoreUp()

    if hania.head.xcor() > 280 or hania.head.xcor() < -280 or hania.head.ycor() > 280 or hania.head.ycor() < -280:
        game_is_on = False
        scoreboard.GameOver()

    for segment in hania.segments:
        if segment == hania.head:
            pass
        elif hania.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.GameOver()






screen.exitonclick()
