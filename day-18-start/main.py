from turtle import Turtle, Screen
import random

stella = Turtle()
screen = Screen()
screen.colormode(255)
stella.speed(0)

# Returns a random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color


# Random Walk
# stella.width(10)
# stella.speed(0)
# direction = [0, 90, 180, 270]
# for _ in range (200):
#     stella.color(random_color())
#     stella.forward(25)
#     stella.setheading(random.choice(direction))


# Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        stella.color(random_color())
        stella.circle(100)
        stella.setheading(stella.heading() + size_of_gap)

draw_spirograph(5)


# Draw shapes
# def draw_shape(num_sides):
#     angle = 360 / sides
#     for _ in range(0, sides):
#         stella.fd(100)
#         stella.rt(angle)
#
# def change_color(sides):
#     colors = ["coral", "blue", "brown", "cyan", "yellow", "black", "green", "purple"]
#     color_index = sides - 3
#     return colors[color_index]
#
#
# for sides in range(3, 11):
#     draw_shape(sides)
#     stella.pencolor(change_color(sides)

screen.exitonclick()

