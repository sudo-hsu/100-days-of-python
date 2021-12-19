# import colorgram
#
# colors = colorgram.extract('hirst_painting.jpg', 30)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     final_rgb = (r, g, b)
#     color_list.append(final_rgb)
#
# print(color_list)
from turtle import Turtle, Screen
import random

screen = Screen()
t = Turtle()
screen.colormode(255)
screen.setworldcoordinates(-1,-1,1000,1000)
t.speed(0)
t.hideturtle()
t.penup()


color_list = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (11, 103, 159), (242, 212, 68), (149, 83, 40), (215, 87, 63),
 (155, 7, 24), (164, 162, 31), (157, 62, 102), (11, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 162),
 (8, 172, 216), (1, 61, 144), (4, 212, 206), (159, 33, 24), (9, 140, 86), (145, 227, 217), (122, 192, 148),
 (220, 177, 216), (101, 218, 229), (119, 173, 193), (80, 134, 178)]


def get_position():
    return t.position()


def draw_dot():
    for _ in range(10):
        random_color = random.choice(color_list)
        t.dot(50, random_color)
        t.goto(get_position() + (100,0))


for y in range(1, 11):
    y_axis = 100
    y_axis *= y
    t.goto(0, y_axis)
    draw_dot()

screen.exitonclick()