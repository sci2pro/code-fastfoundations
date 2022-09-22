import math
import os
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


def main():
    small_circle = Circle(10)
    big_circle = Circle(50)

    print(small_circle)
    print(big_circle)

    # now we change units for all instances on the class
    Circle.units = 'pm'

    print(small_circle)
    print(big_circle)

    # but
    big_circle.units = 'hm'  # only change for the big_circle instance

    print(small_circle)
    print(big_circle)

    # canvas = Canvas(1200, 780)
    # canvas.mystery_method()
    # turtle.done()

    print(small_circle.area())
    print(small_circle.perimeter())
    print(small_circle.arc_length(math.pi * 2.5))
    print(small_circle.bounding_box())

    return os.EX_OK


if __name__ == '__main__':
    sys.exit(main())
