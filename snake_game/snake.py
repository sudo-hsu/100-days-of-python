from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_location = []
        self.starting_x = 0
        self.create_snake()
        self.head = self.snake_location[0]

    def create_snake(self):
        for snake in range(3):
            self.starting_x -= 20
            self.add_segment()

    def add_segment(self):
        new_snake = Turtle(shape="square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(self.starting_x, 0)
        self.snake_location.append(new_snake)

    def extend(self):
        self.add_segment()

    def move(self):
        for snake_num in range(len(self.snake_location) - 1, 0, -1):
            new_x = self.snake_location[snake_num - 1].xcor()
            new_y = self.snake_location[snake_num - 1].ycor()
            self.snake_location[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def reset(self):
        for seg in self.snake_location:
            seg.goto(1000, 1000)
        self.snake_location.clear()
        self.create_snake()
        self.head = self.snake_location[0]