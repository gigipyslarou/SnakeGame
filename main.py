from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

## Setting up the Window ##
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# moving the snake
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.start, "space")
screen.onkey(snake.pause, "p")

game_is_on = True


while game_is_on:
    score.instructions()
    if snake.activate:
        snake.move_snake()
        score.current_score()
        screen.update()
        time.sleep(0.1)
    # 4. Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.points()
# 6. Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

# 7. Detect collision with tail
# if head collides with any segment of the tail:
    # trigger the game over sequence
    for sn in snake.snake_add_on:
        if sn == snake.head:
            pass
        elif snake.head.distance(sn) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()