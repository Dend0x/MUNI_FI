from ib111 import week_00  # noqa
from turtle import forward, left, done, penup, pendown, speed, delay
from math import pi


# Napište proceduru, která bude kreslit soustředné kružnice, a to
# tak, že první má poloměr ‹radius› a zbytek je rovnoměrně rozložen
# tak, aby bylo kružnic celkem ‹count›.

def circle(radius):
    n = 1000
    side = 2 * pi * radius / n
    angle = 360.0 / n

    penup()
    forward(radius)
    left(90)
    pendown()

    for i in range(n):
        forward(side)
        left(angle)
    
    penup()
    left(90)
    forward(radius)
    left(180)
    pendown()

def target(radius, count):
    offset = float(radius) / count
    actual_radius = radius
    for i in range(count):
        circle(actual_radius)
        actual_radius -= offset
        


def main():
    speed(0)
    delay(0)
    target(100, 4)
    done()


if __name__ == "__main__":
    main()
