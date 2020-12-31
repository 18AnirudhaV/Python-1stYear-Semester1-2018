'''
This program draws a picture using the Turtle Graphics module in Python.

~~~~~~~~~~~~~~~~~~~~~~

A picture represents a thousand words - Anonymous

In this picture, I created an abstract piece in which the pig represents those in poverty as they are seen by the higher
up with money as 'pigs'. The pig works day and night in the harsh rains only to be fed his 'money'.

This piece was inspired when I tasted the delicious 'Pork Lo Mein' at Ban Righ.

~~~~~~~~~~~~~~~~~~~~~~

Author: Anirudha Verma
    (Artist in the workings)
Date: 25/09/2018
Student Number: 20128760
'''

# importing Turtle and random, to help draw the picture
import turtle
import random

'''
Draws a square beginning at the upper left corner of the square denoted by startPos.  
startPos is a tuple containing 2 values (x, y) indicating the start position.
The size of the square is denoted by the parameter size (in pixels).
Colour is a string containing a hexidecimal number representing the color.
A hexidecimal number looks something like #FF0000.  So, to represent red, the string
"#FF0000" would be passed as the colour.
Use https://www.webfx.com/web-design/color-picker/ to find colour representations.
'''

def drawSquare(theTurtle, startPos, size, colour):

    # move the turtle to startPos position
    theTurtle.penup()
    theTurtle.setposition(startPos)
    theTurtle.pendown()

    # set the direction of the turtle
    theTurtle.setheading(90)

    # set colour of square
    theTurtle.color(colour)

    # draw the square and fill it
    theTurtle.begin_fill()
    for i in range(4):
        theTurtle.forward(size)
        theTurtle.right(90)
    theTurtle.end_fill()

'''
Draws a 5 point star starting at startx, starty which is the top-most point of the star.
startPos is a tuple containing 2 values (x, y) indicating the start position.
Size is the length of the line from one point to the next. 
Colour is a string containing a hexidecimal number representing the color.  
Use https://www.webfx.com/web-design/color-picker/ to find colours.
'''

def drawStar(theTurtle, startPos,  size, colour):

    # move the turtle to (startx, starty) position
    theTurtle.penup()
    theTurtle.setposition(startPos)
    theTurtle.pendown()

    # set the direction of the turtle
    theTurtle.setheading(90)

    # set colour of star
    theTurtle.color(colour)

    # draw the star and fill it
    theTurtle.begin_fill()
    for i in range(5):
        theTurtle.forward(size)
        theTurtle.right(144)
    theTurtle.end_fill()

'''
Draws an equilateral traingle starting at startx, starty which is the top-most point of the triangle.
startPos is a tuple containing 2 values (x, y) indicating the start position.
Size is the length of the line from one point to the next. 
Colour is a string containing a hexidecimal number representing the color.  
Use https://www.webfx.com/web-design/color-picker/ to find colours.
'''

def drawTriangle(theTurtle, startPos, size, colour):

    # move the turtle to (startx, starty) position
    theTurtle.penup()
    theTurtle.setposition(startPos)
    theTurtle.pendown()

    # set the direction of the turtle
    theTurtle.setheading(90)

    # set colour of triangle
    theTurtle.color(colour)

    # draw the triangle and fill it
    theTurtle.begin_fill()
    for i in range(3):
        theTurtle.forward(size)
        theTurtle.right(120)
    theTurtle.end_fill()

'''
Draws a rectangle starting at startx, starty which is the top-most point of the rectangle.
startPos is a tuple containing 2 values (x, y) indicating the start position.
Size is the length of the line from one point to the next. 
Colour is a string containing a hexidecimal number representing the color.  
Use https://www.webfx.com/web-design/color-picker/ to find colours.
'''

def drawRectangle(theTurtle, startPos, width, length, colour):
    # move the turtle to startPos position
    theTurtle.penup()
    theTurtle.setposition(startPos)
    theTurtle.pendown()

    # set the direction of the turtle
    theTurtle.setheading(90)

    # set colour of the rectangle
    theTurtle.color(colour)

    # draw the rectangle and fill it
    theTurtle.begin_fill()
    for i in range(4):
        theTurtle.forward(width)
        theTurtle.right(90)
        theTurtle.forward(length)
        theTurtle.right(90)
    theTurtle.end_fill()


'''
This draws the money that the pig is working and "eating".
'''
def drawMoney(bob):

    #Using a for loop I create green triangles within a certain area to represent the money
    for moneyCount in range(0, 40, 2):
        drawTriangle(bob, (random.randint(460, 480), random.randint(390, 410)), 10, "#0FBF00")

'''
This draws the box in which the money is held for the pig to work towards and "eat".
'''
def drawMoneyBox(bob):

    #Using for loops I create the money box, it is created using for loops to signify how over time their value increases

    #draws the first tip/peg of the box
    for tip1 in range(0 ,20 ,2):
        drawSquare(bob, (450, 400 + tip1), 10, "#FF27D1")

    #draws the bottom of the box
    for line1 in range(0 ,40 ,2):
        drawSquare(bob, (450 + line1, 420), 10, "#FF27D1")

    #draws the second tip/peg of the box
    for tip2 in range(0, 20, 2):
        drawSquare(bob, (490, 420 - tip2), 10, "#FF27D1")

'''
This draws the stary night in which the pig works in signifying the beauty of the world in which he lives.
But the rain drawn shows the sadness as well.
'''
def drawStaryNights(bob):

    #Using a for loop a stary night is created - random function is used
    for starCount in range(0, 10):
        for position in range(20, 620, 100):
            drawStar(bob, (position, random.randint(50, 500)), 50, "#FFFF00")

    #Using another for loop the harsh rain is created - random function is used
    for rainCount in range(0, 10):
        for position in range(0, 600, 100):
            drawTriangle(bob, (position, random.randint(50, 500)), 10, "#0BE2F2")

'''
This draws the pig. Its body is made out of boxes to represent how he cannot think outside the box.
'''
def drawBoxPig(bob):

    #This draws the body of the pig
    drawSquare(bob, (250, 250), 100, "#FF27D1")
    drawSquare(bob, (150, 250), 100, "#FF27D1")
    drawSquare(bob, (300, 250), 100, "#FF27D1")

    #For loop created to draw the tail of the pig out of triangles
    for tail in range(0,10):
        drawTriangle(bob, (140 - (tail*3), 325 + (tail*2)), 10, "#FF27D1")

    #For loop created to draw the nose of the pig
    for nose in range(0, 2):
        drawSquare(bob, (400 + nose, 275), 10, "#FF27D1")

    #For loop created to draw the ear of the pig
    for ear in range(0, 20, 2):
        drawSquare(bob, (350, 250 - ear), 20, "#FF27D1")

    #draws the legs of the pig
    drawRectangle(bob, (150, 325), 75, 50, "#FF27D1")
    drawRectangle(bob, (275, 325), 75, 50, "#FF27D1")

    #draws the eye of the pig - triangle to make it look angry
    drawTriangle(bob, (380, 280), 10, "#FFFFFF")

'''
The main function starts the program execution.  The drawing area size is set. 
The coordinate system is set so that (0, 0) is in the top left corner of the drawing window.
x increases going to the right, y increases as you move down the screen.  The bottom right corner is 
position (width, height).
A turtle is created (called bob) and is used for drawing.
'''

def main():

    #initializes the screen size and the coordinate system.
    width = 600
    height = 600
    turtle.setup(width, height)
    wn = turtle.Screen()
    wn.setworldcoordinates(0, width, height, 0)

    #sets the background colour to be black.
    turtle.bgcolor("black")


    #creates the turtle with which is drawn.
    bob = turtle.Turtle()
    bob.speed(0)

    #using the draw functions created, it takes an input

    drawStaryNights(bob)
    drawBoxPig(bob)
    drawMoneyBox(bob)
    drawMoney(bob)

    #the following stops the window from closing so that you can admire the drawing
    wn.exitonclick()

main()