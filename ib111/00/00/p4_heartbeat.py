from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, done, speed


# Implementujte proceduru ‹heartbeat›, která vykreslí stylizovanou
# křivku EKG. Parametr ‹iterations› udává počet tepů, které
# procedura vykreslí. Zbylé parametry zadávají amplitudu základního
# úderu a periodu slabšího úderu. Slabší úder má poloviční
# amplitudu.  Například při periodě 3 bude mít sníženou amplitudu
# každý třetí úder, počínaje prvním.

def drawbeat(amplitude):
    forward(10)
    left(75)
    forward(amplitude)
    right(150)
    forward(amplitude * 1.5)
    left(150)
    forward(amplitude * 0.5)
    right(75)
    forward(10)

def heartbeat(amplitude, period, iterations):
    for i in range(1, iterations + 1):
        if(i % period == 0):
            drawbeat(float(amplitude) / 2)
        else:
            drawbeat(amplitude)


def main():
    speed(4)
    heartbeat(30, 3, 5)
    done()


if __name__ == "__main__":
    main()
