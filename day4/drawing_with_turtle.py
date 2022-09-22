import sys
import turtle


def draw_rectangle():
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(10)


def draw_circle():
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(15, 28)
    pen.down()
    pen.begin_fill()
    pen.pencolor("red")
    pen.fillcolor("purple")
    pen.circle(60)
    pen.end_fill()
    pen.up()


def turning_angle(n):
    return 360 / n


def draw_polygon(n, length=10, position=(0, 0), fill='white', stroke='black'):
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(*position)  # we are unpacking position
    pen.pencolor(stroke)
    pen.fillcolor(fill)
    pen.begin_fill()
    pen.down()
    for i in range(n):
        pen.forward(length)
        pen.right(turning_angle(n))
    pen.end_fill()
    pen.up()


def panda():
    import turtle
    pen = turtle.Turtle()

    def ring(col, rad):
        # Set the fill
        pen.fillcolor(col)

        # Start filling the color
        pen.begin_fill()

        # Draw a circle
        pen.circle(rad)

        # Ending the filling of the color
        pen.end_fill()

    pen.up()
    pen.setpos(-35, 95)
    pen.down
    ring('black', 15)

    # Draw second ear
    pen.up()
    pen.setpos(35, 95)
    pen.down()
    ring('black', 15)

    pen.up()
    # pen.


def main():
    # draw_rectangle()
    # draw_circle()
    # draw_polygon(17, length=100, fill="#ccff66", stroke="red", position=(-100, 200))
    panda()
    turtle.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
