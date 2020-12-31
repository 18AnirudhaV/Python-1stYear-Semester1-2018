"""
Anirudha Verma - 20128760
23th October 2018

Assignment 2 - Plotting Functions
"""

from tkinter import *
from math import *

CANV_WIDTH = 750
CANV_HEIGHT = 250

def drawXScale(scale, length):
    """
    This function draws the x-axis ticks.
    scale - distance between each tick
    length - length of each tick
    """
    width = w.winfo_width() // 2

    # Loop through the ticks
    for x in range(0, width, scale):
        # Right side
        w.create_line(get_x(x), get_y(0), get_x(x), get_y(-length))

        # Left side
        w.create_line(get_x(-x), get_y(0), get_x(-x), get_y(-length))

def drawYScale(scale, length):
    """
    This function draws the y-axis ticks.
    scale - distance between each tick
    length - length of each tick
    """
    height = w.winfo_height() // 2

    # Loop through the ticks
    for y in range(0, height, scale):
        # Right side
        w.create_line(get_x(0), get_y(y), get_x(-length), get_y(y))

        # Left side
        w.create_line(get_x(0), get_y(-y), get_x(-length), get_y(-y))

def draw_axes(scaleValue, tickLength):
    """
    Draws a horizontal line across the middle of the canvas, and a vertical
    line down the centre of the canvas using tkinter's default line thickness
    and colour.
    """
    # Draw the x axis
    width = w.winfo_width()
    w.create_line(get_x(-width//2),get_y(0),get_x(width//2),get_y(0))

    # Draw the y axis
    height = w.winfo_height()
    w.create_line(get_x(0),get_y(-height//2),get_x(0),get_y(height//2))

    # Draw the ticks
    drawXScale(scaleValue, tickLength)
    drawYScale(scaleValue, tickLength)
def get_x(x_val):
    """
    Maps a Cartesian-style x coordinate (where x is 0 at the window's
    horizontal centre) onto the tkinter canvas (where x is 0 is at the left
    edge). x_val is the Cartesian x coordinate. The units of measurerment
    are pixels.
    """

    width = w.winfo_width()
    x = width // 2 + x_val

    return x

def get_y(y_val):
    """
    Maps a Cartesian-style y coordinate (where y is 0 at the window's
    vertical centre, and in which y grows in value upwards) onto the tkinter
    canvas (where y is 0 is at the top edge, and y grows in value downwards).
    y_val is the Cartesian y coordinate. The returned value is the
    corresponding tkinter canvas x coordinate. The units of measurerment are
    pixels.
    """

    height = w.winfo_height()
    y = height // 2 + y_val

    return y

def plot_point(x,y,colour='black'):
    """
    Draws a single pixel "dot" at Cartesian coordinates (x,y).
    The optional colour parameter determines the colour of the dot.
    """

    x = get_x(x)
    y = get_y(y)

    w.create_oval(x, y, x, y, width=0, fill=colour)

def plot_fn(fn,start_x,end_x,scale=20,colour='black'):
    """
    Plots a function, y = fn(x), onto the canvas.

    Parameters:

    * fn is a function that takes a single number parameter and returns a
      number.
	  
    * start_x is the left-most x value to be passed to fn.

    * end_x is the right-most x value to be passed to fn.
	
    * scale (optional) is used as a multiplier in both the x and y directions
      to "zoom in" on the plot. It is also used to increase the number of x
      coordinates "fed" to the fn function, to fill in all the horizontal gaps
      that would otherwise appear between the plotted points. scale is
      particularly useful for showing detail that would be otherwise be lost.

    * colour (optional) determines the colour of the plotted function.
	
    Note: nothing bad happens if start_x, end_x, or any y value computed from
    fn(x) is off the canvas. Those points simply will not be displayed.
    (Note to the student programmer: This happens automatically. You don't
    have to program it.)
    """

    for x in range(start_x * scale, end_x * scale):
        y = -scale*fn(x/scale)
        plot_point(x, y, colour)

def square(x):
    """Returns the square of x"""
    return x * x

def func_1(x):
    """A quadratic polynomial function (for testing)."""
    return -3 * square(x) + 2 * x + 1
    
def func_2(x):
    """Exponential Function"""
    return exp(x)

def func_3(x):
    """Tangent Graph"""
    return tan(x)

master = Tk()
master.title('Plot THIS!')
w = Canvas(master,
           width=CANV_WIDTH,
           height=CANV_HEIGHT)
w.pack(expand=YES, fill=BOTH)
w.update() # makes w.winfo_width() and w.winfo_height() meaningful

def main():
    draw_axes(50, 10)
    plot_fn(sin,-20,20,40,'green') # sin() is defined in the math module
    plot_fn(cos,-20,20,40,'blue')  # cos() is defined in the math module
    plot_fn(square,-20,20,40,'red')
    plot_fn(func_1,-20,20,40,'purple')
    plot_fn(func_2,-20,20,40,'brown')
    plot_fn(func_3,-20,20,40,'cyan')
main()

mainloop()
