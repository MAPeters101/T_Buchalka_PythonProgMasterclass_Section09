# import turtle
#
# turtle.pendown()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.done()

import turtle


def square(length: int) -> None:
    """Draws a square of length 'length'"""
    for side in range(4):
        turtle.forward(length)
        turtle.right(90)

for s in range(72):
    square(120)
    turtle.left(5)

turtle.done()
