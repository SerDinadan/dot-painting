import colorgram

# colors = colorgram.extract('hirst-dot-painting.jpg', 20)

# for each_color in range(0, 20):
#     color_list_temp = [colors[each_color].rgb.r, colors[each_color].rgb.g, colors[each_color].rgb.b]
#     color_list.append(tuple(color_list_temp))
import turtle
import random

color_list = [(201, 164, 112), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20),
              (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32),
              (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48)]

timmy = turtle.Turtle()
timmy.speed(10)


def dot_row():
    for row in range(10):
        color_choice = random.choice(color_list)
        timmy.dot(20, color_choice)
        if row < 9:
            timmy.penup()
            timmy.forward(50)
        else:
            timmy.left(90)
            timmy.forward(50)
            timmy.left(90)
            timmy.forward(450)
            timmy.left(180)


screen = turtle.Screen()
screen.setworldcoordinates(-10, -10, 500, 500)
screen.colormode(255)

for column in range(10):
    dot_row()
screen.exitonclick()
