from ib111 import week_00  # noqa
from turtle import forward, left, right, penup, pendown, done, setheading
from math import sqrt, atan, degrees

# Nakreslete obrys vlajky s klínem vlevo (viz obrázky níže).
# Parametry ‹width› a ‹height› (kladná reálná čísla) označují šířku,
# resp. výšku vlajky. Parametr ‹triangle_ratio› (reálné číslo mezi 0
# a 1 včetně) označuje, do jaké části šířky vlajky má zasahovat její
# klín.

def outer_part(width, height):
    for i in range(4):
        if i % 2 == 0:
            forward(width)
        else:
            forward(height)
        left(90)

def flag(width, height, triangle_ratio):
    outer_part(width, height)
    triangle_height = width * triangle_ratio
    triangle_side = sqrt(triangle_height ** 2 + (height / 2.0) ** 2)
    triangle_angle = degrees(atan(triangle_height / (height / 2.0)))
    print(triangle_angle)

    left(90 - triangle_angle)
    forward(triangle_side)
    left(2 * triangle_angle)
    forward(triangle_side)

def main():
    flag(150, 100, 0.5)

    penup()
    setheading(0)
    forward(200)
    right(90)
    forward(125)
    left(90)
    pendown()

    flag(100, 150, 0.3)
    done()


if __name__ == "__main__":
    main()
