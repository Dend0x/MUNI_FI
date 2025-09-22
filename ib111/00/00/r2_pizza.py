from ib111 import week_00  # noqa
from turtle import forward, left, right, penup, pendown, \
    setheading, done, delay, speed
from math import pi

# † Nakreslete kruhovou výseč („dílek pizzy“) se středovým úhlem
# zadaným (v stupních) parametrem ‹angle› a délkou strany ‹side›.

def pizza(side, angle):
    n = 1000
    sector_of_a_circle_length_forward = 2 * pi * side / 360.0 * angle / n
    sector_of_a_circle_angle = float(angle) / n
    forward(side)
    left(90)
    for i in range(n):
        forward(sector_of_a_circle_length_forward)
        left(sector_of_a_circle_angle)

    left(90)
    forward(side)


def main():
    delay(0)
    speed(1)
    pizza(70, 65)

    penup()
    setheading(0)
    forward(150)
    pendown()

    pizza(100, 25)

    done()


if __name__ == "__main__":
    main()
