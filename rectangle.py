'''
File: rectangle.py
Purpose: A class for creating rectangles. Collaborates with the Points class
Author: Dr. Scott Heggen
Acknowledgements: Much of the code is originally from: http://openbookproject.net/thinkcs/python/english3e/
'''

import turtle

class Rectangle():
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn          # A Point object to hold the bottom left corner of the rectangle
        self.width = w
        self.height = h

    def __str__(self):
        '''
        Overriden string class which allows the user to use str() to print cleanly
        :return:
        '''
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def draw_rectangle(self, r=0, g=0, b=0, angle=0, text = ""): # black is the default color
        ''' instantiates a Turtle object and draws the Rectangle on the Screen at an angle, and tags it with a text.
            Notice the turtle is implemented differently here than in the Point class,
            as a demonstration of the many ways in which we can implement the same thing. '''
        turt = turtle.Turtle()
        turt.color(r, g, b)
        turt.penup()
        # self.corner refers to a Point object, so self.corner.x refers to the x-coordinate;
        # self.corner.y refers to the y-coordinate
        turt.goto(self.corner.x, self.corner.y)
        # rotates to turtle by angle degrees
        turt.left(angle)
        turt.showturtle()
        turt.pendown()
        # draws the rectangle to the screen
        for i in range(2):
            turt.forward(self.width)
            turt.left(90)
            turt.forward(self.height)
            turt.left(90)
        # writes custom text to the screen if provided;
        # else prints the starting coordinates, width, and height of the rectangle
        if text == "":
            turt.write(str(self), True)
        else:
            turt.write(text, True)
        turt.hideturtle()
