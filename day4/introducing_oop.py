import math
import sys
import turtle


class Circle:
    units = 'cm'  # all circles will have the same units

    def __init__(self, radius, position=(0, 0), fill='white', stroke='black'):
        self.radius = radius  # each circle will have a particular radius
        self.position = position
        self.fill = fill
        self.stroke = stroke

    def __str__(self):  # Python special methods
        return f"I am a circle of size {self.radius}{self.units} located at {self.position}."

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def arc_length(self, angle, degrees=False):
        """Function to compute the arc length l for the angle provided"""
        if degrees:  # angle is in degrees
            return self.radius * math.radians(angle)
        return self.radius * angle  # assume angle is in radians

    def bounding_box(self):
        """Function to compute the four values of the bounding box for a circle"""
        # xmin, xmax, ymin, ymax
        return (
            self.position[0] - self.radius,
            self.position[0] + self.radius,
            self.position[1] - self.radius,
            self.position[1] + self.radius,
        )

    def draw(self, pen):
        if pen.isdown():
            pen.up()
        pen.goto(*self.position)
        pen.down()
        pen.begin_fill()
        pen.pencolor(self.stroke)
        pen.fillcolor(self.fill)
        pen.circle(self.radius)
        pen.end_fill()
        pen.up()


class Rectangle:
    def __init__(self, width, height, position=(0, 0), fill='white', stroke='black', angle=0.0):
        self.width = width
        self.height = height
        self.position = position
        self.fill = fill
        self.stroke = stroke
        self.angle = angle

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def bounding_box(self):
        return (
            self.position[0] - self.width / 2,
            self.position[0] + self.width / 2,
            self.position[1] - self.height / 2,
            self.position[1] + self.height / 2,
        )

    def __str__(self):
        return f"Rectangle: ({self.width}x{self.height}) loc: {self.position}"

    def draw(self, pen):
        if pen.isdown():
            pen.up()
        pen.goto(*self.position)
        pen.down()
        pen.begin_fill()
        pen.pencolor(self.stroke)
        pen.fillcolor(self.fill)
        pen.forward(self.width)
        pen.right(90)
        pen.forward(self.height)
        pen.right(90)
        pen.forward(self.width)
        pen.right(90)
        pen.forward(self.height)
        pen.right(90)
        pen.end_fill()
        pen.up()


class Square(Rectangle):
    def __init__(self, width, *args, **kwargs):
        super().__init__(width, width, *args, **kwargs)


class Canvas(turtle.TurtleScreen):
    def __init__(self, width, height, bg="white"):
        canvas = turtle.getcanvas()
        super().__init__(canvas)
        self.screensize(width, height, bg=bg)
        self.width = width
        self.height = height
        self.pen = turtle.RawTurtle(canvas)

    def draw(self, shape):
        shape.draw(self.pen)

    def mystery_method(self):
        self.pen.up()
        self.pen.goto(0, self.height / 2)
        self.pen.down()
        self.pen.goto(0, -self.height / 2)
        self.pen.up()
        self.pen.goto(-self.width / 2, 0)
        self.pen.down()
        self.pen.goto(self.width / 2, 0)
        self.pen.up()
        self.pen.home()

    def __str__(self):
        return f"Canvas of dimensions ({self.width}, {self.height})"


class Text:
    def __init__(self, text, position=(0, 0), colour='black'):
        self.text = text
        self.position = position
        self.colour = colour

    def __str__(self):
        return self.text


def main():
    rectangle = Rectangle(37, 40, position=(-15, -15))
    print(rectangle)
    square = Square(30)
    print(square)
    print(square.angle)
    # make a Canvas object
    canvas = Canvas(1200, 750, bg="#555555")
    print(canvas)
    # canvas.mystery_method()
    small_circle = Circle(30, fill='red', stroke='purple')
    big_circle = Circle(100, position=(20, -10), fill='yellow', stroke='green')
    canvas.draw(big_circle)
    canvas.draw(small_circle)
    rectangle = Rectangle(60, 28, position=(-15, -15), fill='grey', stroke='indigo')
    canvas.draw(rectangle)
    turtle.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
