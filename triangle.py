import turtle
import math

def triangle(size):
    """
    rysowanie trojkata
    :param size: bok
    :return:
    """
    t = turtle.Pen()
    t.forward(size)
    t.right(90+45)
    t.forward(size*math.sqrt(2))
    t.right(90+45)
    t.forward(size)

triangle(100)
triangle(200)
triangle(300)

turtle.Screen().exitonclick()