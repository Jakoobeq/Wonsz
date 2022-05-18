from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:


    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]


    def create_snake(self):
        for position in POSITIONS:
            self.add_body_part(position)


    def movement(self):
        for body_number in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_number - 1].xcor()
            new_y = self.snake_body[body_number - 1].ycor()
            self.snake_body[body_number].goto(new_x, new_y)
        self.head.color("dark green")
        self.head.forward(MOVE_DISTANCE)


    def extend(self):
        self.add_body_part(self.snake_body[-1].position())


    def add_body_part(self, position):
        snake = Turtle("square")
        snake.color("light green")
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

