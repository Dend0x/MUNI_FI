from ib111 import week_04  # noqa


# Čistá funkce ‹gambling_score› ohodnotí výsledek hozený na kostkách
# (neprázdný seznam celých čísel od 1 do 6 včetně) takto:
#
# Trojice stejných čísel se boduje jako 100× hozené číslo, kromě trojice
# jedniček, která je za 1000. Čtveřice stejných čísel se počítá za
# dvojnásobek hodnoty trojice, pětice se počítá za dvojnásobek hodnoty
# čtveřice atd. Pokud po započítání všech trojic, čtveřic, pětic atd. zbudou
# nějaké (dosud nezapočítané) jedničky a pětky, počítá se každá jednička za
# sto bodů, každá pětka za padesát bodů. Získané body se sečtou.
#
# Příklad: Pro vstup ‹[1, 1, 1, 1, 5, 3, 3, 3, 4]› funkce vrátí ‹2350›
# (čtveřice jedniček za 2000 bodů, trojice trojek za 300 bodů, jedna pětka
# za 50).
# Pro vstup ‹[2, 2, 5, 2, 2, 5, 2, 2]› funkce vrátí ‹1700›
# (šestice dvojek za 1600 bodů, dvě pětky za 100).
# Pro vstup ‹[2, 2, 3, 4, 6, 6]› funkce vrátí ‹0›
# (není zde žádná trojice ani lepší skupina stejných čísel, žádné jedničky,
# žádné pětky).
#
# Všimněte si zejména, že na pořadí čísel v seznamu nezáleží a že počítáme
# vždy maximální množství výskytů daného čísla (tedy poté, co jsme v prvním
# příkladu započítali čtveřici jedniček za 2000 bodů, už neuvažujeme o tom,
# kolik trojic jedniček v seznamu je).


def gambling_score(dice):
    counts = [0,0,0,0,0,0]
    result = 0

    for number in dice:
        counts[number - 1] += 1

    for index, count in enumerate(counts):
        index += 1
        if count >= 3:
            to_sum = 0
            if index == 1:
                to_sum = 1000
            else:
                to_sum = index * 100

            for i in range(3, count):
                to_sum *= 2

            result += to_sum
        if index == 1:
            if count != 3 and count != 4 and count != 5:
                result += count * 100
        if index == 5:
            if count != 3 and count != 4 and count != 5:
                result += count * 50
    return result


def main() -> None:
    dice = [1, 1, 1, 1, 5, 3, 3, 3, 4]
    assert gambling_score(dice) == 2350
    assert dice == [1, 1, 1, 1, 5, 3, 3, 3, 4]

    assert gambling_score([2, 2, 5, 2, 2, 5, 2, 2]) == 1700
    assert gambling_score([2, 2, 3, 4, 6, 6]) == 0
    assert gambling_score([5, 5, 5, 5, 5]) == 2000
    assert gambling_score([6, 6, 6, 6, 6, 6]) == 4800
    assert gambling_score([1, 2, 3, 4, 5, 6]) == 150
    assert gambling_score([2, 4, 3, 4, 6, 4]) == 400


if __name__ == '__main__':
    main()
