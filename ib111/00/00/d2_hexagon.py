from ib111 import week_00  # noqa
from turtle import forward, left, done, speed


# V této ukázce sestrojíme „segmentovaný“ šestiúhelník složením
# z 6 pootočených rovnostranných trojúhelníků. Smyslem je ukázat,
# že část výpočtu si můžeme pojmenovat, a poté ji s výhodou využít
# jako stavební kámen něčeho složitějšího. V tomto případě se vybízí
# pojmenovat si právě vykreslení onoho rovnostranného trojúhelníku:

def triangle():
    for i in range(3):
        forward(100)
        left(120)


# To, co jsme právě udělali, se obecně jmenuje «definice podprogramu».
# V tomto případě se jedná konkrétně o «proceduru», totiž
# podprogram, kterého smyslem je provést nějaké «akce» (vedlejší
# efekty). V našem případě je tedy ‹triangle› procedurou pro
# vykreslení rovnostranného trojúhelníku. Naše nově definovaná
# procedura ‹triangle› je k nerozeznání od těch zabudovaných
# (knihovních), které známe z předchozí ukázky: ‹left›,
# ‹forward› a pod.

def hexagon():
    for i in range(6):
        triangle()
        left(360.0 / 6)


# Teď již víme, že ‹main› je také procedura, tedy podprogram,
# kterého smyslem je vykonat posloupnost akcí (typicky dalších
# procedur).

def main():  # demo
    speed(5)
    hexagon()
    done()


if __name__ == "__main__":
    main()
