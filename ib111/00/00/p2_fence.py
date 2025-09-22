from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, done, speed


# Napište program, který nakreslí „plot“ o délce ‹length› pixelů,
# složený z prken (obdélníků) o šířce ‹plank_width› a výšce
# ‹plank_height›. Přesahuje-li poslední prkno požadovanou délku
# plotu, ořežte jej tak, aby měl plot přesně délku ‹length›.
# Zamyslete se nad rozdělením vykreslování do několika samostatných
# procedur. Při kreslení se vám také může hodit while cyklus.

def plank(plank_width, plank_height):
    for i in range(4):
        if i % 2 == 0:
            forward(plank_width)
        else:
            forward(plank_height)
        left(90)

def fence(length, plank_width, plank_height):
    fence_width = 0
    while(length > fence_width):
        if length - fence_width < plank_width:
            plank(length - fence_width, plank_height)
            forward(length - fence_width)
            return
        else:
            plank(plank_width, plank_height)
        fence_width += plank_width
        forward(plank_width)


def main():
    speed(4)
    fence(140, 40, 100)
    done()


if __name__ == "__main__":
    main()
