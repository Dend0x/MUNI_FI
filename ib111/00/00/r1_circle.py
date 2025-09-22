from ib111 import week_00  # noqa
from turtle import speed, delay, forward, backward, left, \
    right, penup, pendown, done
from math import pi

# Pomocí procedury pro mnohoúhelníky si nejprve zkuste vykreslit
# kružnici. Poté napište proceduru pro vykreslení kružnice o zadaném
# poloměru ‹radius›. (Nápověda: srovnejte obvod kružnice a
# pravidelného n-úhelníku). Kružnici nakreslete tak, aby její střed
# ležel v bodě, ve kterém byla želva před použitím procedury
# ‹circle›.  Pro vypnutí a zapnutí kreslení použijte procedury
# ‹penup› a ‹pendown›. Po dokreslení kružnice vraťte želvu zpět do
# jejího středu.

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
    right(90)



def main():
    speed(0)
    delay(0)

    circle(90)
    penup()
    forward(90)
    pendown()

    circle(60)
    penup()
    forward(210)
    pendown()

    circle(30)
    done()


if __name__ == "__main__":
    main()
