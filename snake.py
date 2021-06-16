from turtle import Turtle, Screen

STARTING_SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_add_on = []
        self.create_snake()
        self.head = self.snake_add_on[0]
        self.activate = False

    # Creating the body of the snake:
    def create_snake(self):
        for positions in STARTING_SNAKE_POSITIONS:
            self.snake_plus_one(positions)

# 2. Move the snake

    def move_snake(self):
        for snake_num in range(len(self.snake_add_on) - 1, 0, -1):
            new_x = self.snake_add_on[snake_num - 1].xcor()
            new_y = self.snake_add_on[snake_num - 1].ycor()
            self.snake_add_on[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Adding Turtle onto snake
    def snake_plus_one(self, positions):
        snake = Turtle()
        snake.color("white")
        snake.shape("square")
        snake.penup()
        snake.goto(positions)
        self.snake_add_on.append(snake)

    # Making the snake larger with Food
    def extend(self):
        self.snake_plus_one(self.snake_add_on[-1].position())

    # 3. Control the snake
    def up(self):
        self.head.seth(90)

    def down(self):
        self.head.seth(270)

    def left(self):
        self.head.seth(180)

    def right(self):
        self.head.seth(0)

    def start(self):
        self.activate = True

    def pause(self):
        self.activate = False
