"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Trey Kline.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    #two_circles()
    #circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------
    winder = rg.RoseWindow()
    circle1 = rg.Circle(rg.Point(100, 100), 10)
    circleA = rg.Circle(rg.Point(150, 150), 50)
    circle1.fill_color = 'blue'
    circle1.attach_to(winder)
    circleA.attach_to(winder)
    winder.render()
    winder.close_on_mouse_click()

def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()
    circleCenter = rg.Point(100, 100)
    circleColor = 'blue'
    circleThickness = 4
    rectangleColor = 'purple'
    rectangleThickness = 0.05
    circle = rg.Circle(circleCenter, 10)
    circle.fill_color = circleColor
    circle.outline_thickness = circleThickness
    rectangle = rg.Rectangle(rg.Point(50, 150), rg.Point(150, 60))
    rectangle.attach_to(window)
    circle.attach_to(window)
    window.render()
    window.close_on_mouse_click()
    rectangleCenter = rectangle.get_center()
    print(circleThickness)
    print(circleColor)
    print(circleCenter)
    print(circleCenter.x)
    print(circleCenter.y)
    print(rectangleThickness)
    print(rectangleColor)
    print(rectangleCenter)
    print(rectangleCenter.x)
    print(rectangleCenter.y)


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # DONE: 4. Implement and test this function.
    justFunk30x = rg.RoseWindow()
    line = rg.Line(rg.Point(5, 5), rg.Point(100, 105))
    thiccLine = rg.Line(rg.Point(10, 60), rg.Point(150, 50))
    thiccLine.thickness = 30
    line.attach_to(justFunk30x)
    thiccLine.attach_to(justFunk30x)
    justFunk30x.render()
    midpointPoint = thiccLine.get_midpoint()
    print(midpointPoint)
    print(midpointPoint.x)
    print(midpointPoint.y)
    justFunk30x.close_on_mouse_click()



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
