from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

game = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


def inputs():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


while game:
    inputs()
    time.sleep(0.05)
    screen.update()
    snake.movement()

    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend()
        score.score_track()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game = False
        score.game_over()

    for part in snake.snake_body[1:]:
        if snake.head.distance(part) < 10:
            game = False
            score.game_over()

screen.exitonclick()