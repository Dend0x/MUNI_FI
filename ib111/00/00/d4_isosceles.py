from ib111 import week_00  # noqa


# Doposud jsme se nezabývali otázkou, odkud pochází definice
# procedur ‹left›, ‹forward› apod. Protože ale v této ukázce budeme
# potřebovat další knihovní podprogramy, je čas zmínit existenci
# příkazu ‹import›. Tím oznámíme interpretu Pythonu, že hodláme
# využívat podprogramy z externích «modulů». V tomto kurzu se
# omezíme na moduly ze «standardní knihovny», totiž takové, které
# jsou dodávány s každým interpretem jazyka Python.

# Pro úplnost dodáme, že «modul» je sbírka vzájemně souvisejících,
# znovupoužitelných podprogramů (a případně i složitějších
# artefaktů, kterými se ale nebudeme v tomto kurzu příliš zabývat).

from turtle import forward, left, penup, pendown, done, \
    setheading, speed

# Krom procedur pro práci se želvou budeme v tomto příkladu
# potřebovat několik matematických «funkcí»:
#
#  • odmocninu, realizovanou podprogramem ‹sqrt›,
#  • převod stupňů na radiány, realizovaný podprogramem ‹radians›,
#  • goniometrickou funkci «tangens», realizovanou podprogramem
#    ‹tan›.
#
# Podprogramům, které realizují výpočet nějaké hodnoty na základě
# hodnot svých parametrů, budeme říkat «čisté funkce», z důvodu
# jejich podobnosti s funkcemi z matematiky. Podprogramy ‹sqrt›,
# ‹radians› a ‹tan› jsou tedy v tomto smyslu (čistými) funkcemi.

from math import sqrt, radians, tan


# Krom použití «funkcí» si v této ukázce předvedeme také použití
# «proměnných». V nejjednodušším smyslu je proměnná pouze
# pojmenováním nějaké vypočtené hodnoty – takto je budeme nyní
# používat. Složitější případy použití proměnných (zejména
# «přiřazení») si necháme na příští týden.

# Obrázek, který budeme kreslit, je «rovnoramenný trojúhelník», zadaný
# délkou základny a úhlem (v stupních) mezi základnou a ramenem.

def isosceles(base, angle):

    # První hodnotou, kterou si pojmenujeme (uložíme do proměnné)
    # bude polovina základny: rovnoramenný trojúhelník si totiž
    # pomyslně rozdělíme na dva stejné (pouze zrcadlově otočené)
    # pravoúhlé trojúhelníky s odvěsnami ‹height› (výška) a
    # ‹half_base› (polovina základny).

    half_base = float(base) / 2

    # Protože trojúhelník máme zadaný základnou a přilehlým úhlem,
    # potřebujeme vypočítat délku ramene. To se nejsnadněji provede
    # pomocí už zmíněného pomyslného pravoúhlého trojúhelníku.  Na
    # výpočet délky ramene použijeme Pythagorovu větu, ale nejprve
    # potřebujeme znát výšku (druhou z odvěsen pomyslného
    # trojúhelníku). Protože máme úhel zadaný v stupních, musíme ho
    # nejprve převést na radiány, pak jednoduše použijeme funkci
    # tangens, která udává poměr odvěsen v pravoúhlém trojúhelníku
    # (protilehlá k přilehlé). Výšku získáme jednoduchou úpravou
    # definičního výrazu.

    height = half_base * tan(radians(angle))

    # Konečně můžeme přistoupit k výpočtu délky ramene:

    side = sqrt(height ** 2 + half_base ** 2)

    # Nyní máme vše, co k vykreslení potřebujeme. Nejprve nakreslíme
    # základnu, poté želvu otočíme o «vedlejší úhel» k ‹angle› (tak,
    # aby úhel sevřený základnou a ramenem, které budeme kreslit
    # jako další byl ‹angle›). Vrcholový úhel je daný vztahem ‹180 -
    # 2 * angle›, nicméně opět potřebujeme želvu otočit o příslušný
    # vedlejší úhel (hodnotu ‹2 * angle› dostaneme opět jednoduchou
    # úpravou). Nakonec vykreslíme druhé rameno, a želva se tím
    # vrátí do výchozí pozice.

    forward(base)
    left(180 - angle)
    forward(side)
    left(2 * angle)
    forward(side)


# Abychom ověřili, že program pracuje správně, vykreslíme si dva
# různé trojúhelníky.

def main():  # demo
    speed(5)
    isosceles(100, 45)

    penup()
    setheading(0)
    forward(150)
    pendown()

    isosceles(120, 65)
    done()


if __name__ == "__main__":
    main()
