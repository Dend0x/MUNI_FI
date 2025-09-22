from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, done, \
    penup, pendown, speed
from math import sqrt

# Napište proceduru, která nakreslí „tunel“ – sekvenci soustředných
# čtverců, kde vnější má stranu délky ‹size› a každý další je
# o ‹step› jednotek menší.

def draw_square(size):
    for i in range(4):
        forward(size)
        left(90)

def tunnel(size, step):
    actual_size = size
    while(actual_size > 0):
        draw_square(actual_size)
        actual_size -= step
        penup()
        left(45)
        forward(float(step) / sqrt(2))
        right(45)
        pendown()



def main():
    speed(5)
    tunnel(150, 30)
    done()


if __name__ == "__main__":
    main()
