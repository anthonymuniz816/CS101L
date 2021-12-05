#Anthony Muniz
#Program 12
#CS 101 Lab

#Problem: Need to develop a program that will draw and fill a box and a circle

#Algorithm:
#START
#Import the turtle module
#Create parent class called Point
#Within class define the parameters and create two other functions that will draw
#using the turtle module
#Create another class called Box that will inheret the parent class
#Define parameters within this class and create a function that will draw a box
#Create another class that will inheret the Box class
#Define paramterswithin class and create a function that will fill in the box
#Create another class called circle that will inheret the parent function
#Within class define paramters and create a function that will draw a circle
#Create another class and inheret the circle class
#Within class define parameters and create a fucntion that will fill the circle
#END

import turtle
class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self,x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height

    def draw_action(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        
class BoxFilled(Box):
    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius

    def draw_action(self):
        turtle.circle(self.radius)

class CircleFilled(Circle):
    def __init__(self,x1, y1, radius, color, fill_color):
        super().__init__(x1, y1, radius, color)
        self.fill_color = fill_color

    def draw_action(self):
        turtle.fillcolor(self.fill_color)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()
    
p = Point(-100, 100, 'blue')
p.draw()

b = Box(100, 110, 50, 40, 'pink')
b.x

b1 = BoxFilled(100, 110, 50, 40, 'pink', 'yellow')
b1.draw()

c= Circle(-200, 210, 50, 'purple')
c.draw()

c1 = CircleFilled(-200, 210, 50, 'purple', 'red')
c1.draw()
