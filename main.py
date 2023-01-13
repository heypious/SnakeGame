import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    scoreboard.display()
    screen.update()
    time.sleep(0.2)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update()

    headx = snake.head.xcor()
    heady = snake.head.ycor()
    if headx > 280 or headx < -280 or heady > 280 or heady < -280:
        game_is_on = False
        scoreboard.over()

    for segment in snake.segments:
        if snake.head.distance(segment) < 10 and segment != snake.head:
            game_is_on = False
            scoreboard.over()

screen.exitonclick()
