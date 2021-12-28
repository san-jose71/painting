from turtle import Turtle, Screen
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = Turtle()

tim.shape("arrow")
tim.color("black")


color_list = [(28, 108, 162), (190, 40, 82), (232, 160, 57), (232, 214, 89), (220, 138, 174), (140, 108, 58),
              (106, 193, 215), (22, 57, 130), (199, 167, 35), (209, 76, 94), (235, 89, 53), (119, 191, 143),
              (13, 150, 88), (143, 208, 224), (107, 107, 195), (137, 30, 72), (11, 184, 175), (97, 51, 37),
              (24, 158, 206), (227, 169, 187), (85, 46, 33), (156, 212, 190), (34, 46, 84), (171, 185, 220),
              (31, 89, 92), (28, 95, 92), (233, 173, 159), (242, 204, 5), (92, 24, 51), (23, 73, 70)]



tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dot = 100

for dot_count in range(1, number_of_dot + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



















screen = Screen()
screen.exitonclick()