import math
import sys


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


class Rectangle:
    def __init__(self, width, height, position=(0, 0), fill='white', stroke='black'):
        self.width = width
        self.height = height
        self.position = position
        self.fill = fill
        self.stroke = stroke

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


class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height


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
    return 0


if __name__ == "__main__":
    sys.exit(main())
