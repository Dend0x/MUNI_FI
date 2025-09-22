from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, done, speed, delay


# Napište proceduru pro vykreslení stylizovaného diamantu. Tento se
# skládá z mnohoúhelníků, které jsou vůči sobě natočené o vhodně
# zvolený malý úhel (takový, aby byl výsledný obrazec pravidelný).
# Každý mnohoúhelník má ‹sides› stran o délce ‹length› pixelů.

def draw_polygon(sides, length, angle):
    for i in range(sides):
        forward(length)
        left(angle)

def diamond(sides, length):
    angle = 360.0 / sides
    for i in range(sides):
        draw_polygon(sides, length, angle)
        right(angle)


def main():
    speed(1)
    delay(0)
    diamond(12, 30)
    done()


if __name__ == "__main__":
    main()
