from ib111 import week_00  # noqa
from turtle import forward, left, right, penup, pendown, \
    setheading, done, speed
from math import degrees, atan, sqrt


# Nakreslete rovnoramenný lichoběžník s délkami základen
# ‹base_length› a ‹top_length› a výškou ‹height› (lichoběžník je
# čtyřúhelník s jednou dvojicí rovnoběžných stran – základen –
# spojených rameny, které jsou obecně různoběžné).

def trapezoid(base_length, top_length, height):
    overflowing_side_piece = float(base_length - top_length) / 2
    angle = degrees(atan(float(height) / overflowing_side_piece))
    side_edge = sqrt(overflowing_side_piece ** 2 + height ** 2)
    print(angle)
    forward(base_length)
    left(180 - angle)
    forward(side_edge)
    left(angle)
    forward(top_length)
    left(angle)
    forward(side_edge)
    left(180 - angle)

    


def main():
    speed(4)
    trapezoid(100, 70, 70)

    penup()
    setheading(0)
    forward(150)
    pendown()

    trapezoid(120, 30, 35)

    done()


if __name__ == "__main__":
    main()
