from rectangle import Rectangle
from point import Point
import random
import turtle


def main():
    wn = turtle.Screen()
    wn.colormode(255)

    for i in range(25):
        p = Point(random.randrange(500)-250, random.randrange(500)-250)
        rect = Rectangle(p, random.randrange(i+100), random.randrange(i+100))
        rect.draw_rectangle(random.randrange(255), random.randrange(255), random.randrange(255), random.randrange(360), " ")
    wn.exitonclick()

main()
