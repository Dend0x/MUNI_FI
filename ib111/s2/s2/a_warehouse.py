from ib111 import week_05  # noqa


# V tomto úkolu se budeme zabývat skladem zboží. Zboží je ve skladu uloženo po
# balících, které reprezentujeme trojicemi hodnot: množství (počet jednotek)
# zboží, jednotková cena zboží a datum exspirace. Všechny tři hodnoty budou
# vždy kladná celá čísla, přičemž datum exspirace bude vždy zadáno tak,
# aby jeho zápis v desítkové soustavě byl ve formátu ‹YYYYMMDD› dle ISO 8601.

Package = tuple[int, int, int]  # amount, price, expiration date


# Obsah skladu budeme reprezentovat seznamem balíků, přičemž tento seznam bude
# vždy seřazen sestupně dle data exspirace. (Je zájmem společnosti, které sklad
# patří, aby se jako první prodaly balíky, jejichž konec trvanlivosti se blíží;
# přitom balíky budeme prodávat od konce seznamu.)
#
# Nejprve implementujte funkci ‹remove_expired›, která ze skladu odstraní
# všechny balíky s prošlou trvanlivostí (tj. ty, jejichž datum exspirace
# předchází dnešnímu datu ‹today›, které je zadáno stejně jak je popsáno výše).
# Funkce vrátí seznam odstraněných balíků v opačném pořadí, než byly umístěny
# ve skladu.

def remove_expired(warehouse: list[Package],
                   today: int) -> list[Package]:
    if warehouse == []:
        return []
    left = 0
    right = len(warehouse)

    while left < right:
        middle = (left + right) // 2
        _, _, expiration = warehouse[middle]
        if expiration >= today:
            left = middle + 1
        else:
            right = middle

    result = []

    for i in range(len(warehouse) - left):
        result.append(warehouse.pop())

    return result

# Dále pak implementujte funkci ‹try_sell›, která uskuteční prodej při zadaném
# maximálním množství ‹max_amount› a zadané maximální průměrné jednotkové ceně
# ‹max_price›. Přitom je cílem prodat co nejvíce zboží (v rámci respektování
# zadaných limitů). Prodávat je možno jak celé balíky, tak i jen jejich části;
# je tedy dovoleno existující balík rozbalit a odebrat z něj jen několik
# jednotek zboží (tím vlastně z jednoho balíku vzniknou dva – jeden zůstane ve
# skladu, druhý se dostane ke kupci). Je ovšem třeba postupovat tak, že se
# balíky odebírají pouze z konce seznamu reprezentujícího sklad – tj. není
# možno prodat balík (nebo jeho část), aniž by předtím byly prodány všechny
# balíky nacházející se v seznamu za ním. Funkce vrátí seznam balíků, které se
# dostaly ke kupci, a to v tom pořadí, jak se postupně ze skladu odebíraly.
#
# Pro příklad uvažujme sklad s následujícími balíky (datum exspirace zde
# neuvádíme, horní číslo je množství, spodní cena; pořadí balíků odpovídá
# seřazení seznamu, prodáváme tedy „zprava“):
#
#  ╭─────╮  ╭─────╮  ╭─────╮  ╭─────╮
#  │ 200 │  │  90 │  │ 100 │  │  42 │
#  ├─────┤  ├─────┤  ├─────┤  ├─────┤
#  │ 158 │  │  14 │  │  17 │  │  9  │
#  ╰─────╯  ╰─────╯  ╰─────╯  ╰─────╯
#     D        C        B        A
#
# • Pokud by přišel požadavek na prodej s maximálním množstvím 500 a maximální
#   průměrnou jednotkovou cenou 9, pak se prodá pouze celý balík ‹A›.
# • Pokud by místo toho byla požadovaná maximální průměrná cena 12, pak se
#   prodá celý balík ‹A› a 25 jednotek zboží z balíku ‹B›.
#   (Balík ‹B› se tedy rozdělí: ve skladu zůstane balík s množstvím 75, ke
#   kupci se dostane balík s množstvím 25.)
# • Pokud by byla požadovaná maximální průměrná cena 14, pak se prodá celý
#   balík ‹A› a 70 jednotek zboží z balíku ‹B›.
# • Pokud by byla požadovaná maximální průměrná cena 15, pak se prodají celé
#   balíky ‹A›, ‹B› a ‹C›.
# • Pokud by byla požadovaná maximální průměrná cena 16, pak se prodají celé
#   balíky ‹A›, ‹B›, ‹C› a dvě jednotky zboží z balíku ‹D›.
# • Konečně pro maximální průměrnou cenu 81 se prodají všechny balíky.


def find_max_sell_price(amount_pkg: int, sum_price: int, price_pkg: int,
                        max_price: int, sum_amount: int) -> int:
    left = 0
    right = amount_pkg

    while left < right:
        middle = (left + right) // 2

        if sum_price + middle * price_pkg <= max_price * (sum_amount + middle):
            left = middle + 1
        else:
            right = middle
    return left - 1


def try_sell(warehouse: list[Package],
             max_amount: int, max_price: int) -> list[Package]:

    sum_amount = 0
    sum_price = 0
    result = []

    for i in range(len(warehouse) - 1, -1, -1):
        amount_pkg, price_pkg, _ = warehouse[i]
        sum_amount += amount_pkg
        sum_price += price_pkg * amount_pkg

        if sum_price > sum_amount * max_price:
            prev_sum_price = sum_price - price_pkg * amount_pkg
            prev_sum_amount = sum_amount - amount_pkg

            left = find_max_sell_price(amount_pkg, prev_sum_price,
                                       price_pkg, max_price, prev_sum_amount)

            left_amount = max_amount - prev_sum_amount
            left = min(left, left_amount)

            cur_amount_pkg, cur_price_pkg, ex = warehouse.pop()
            warehouse.append((cur_amount_pkg - left, cur_price_pkg, ex))

            if left > 0:
                result.append((left, cur_price_pkg, ex))

            return result

        if sum_amount > max_amount:
            left_amount = max_amount - sum_amount + amount_pkg
            cur_amount_pkg, cur_price_pkg, ex = warehouse.pop()
            warehouse.append((cur_amount_pkg - left_amount, cur_price_pkg, ex))

            if left_amount > 0:
                result.append((left_amount, cur_price_pkg, ex))

            return result

        result.append(warehouse.pop())

    return result


def main() -> None:
    pkgD = (200, 158, 20771023)
    pkgC = (90, 14, 20220202)
    pkgB = (100, 17, 20220202)
    pkgA = (42, 9, 20211111)
    pkgs = [pkgD, pkgC, pkgB, pkgA]

    store = pkgs.copy()
    assert try_sell(store, 500, 9) == [pkgA]
    assert store == [pkgD, pkgC, pkgB]

    store = pkgs.copy()
    assert try_sell(store, 500, 12) == [pkgA, (25, 17, 20220202)]
    assert store == [pkgD, pkgC, (75, 17, 20220202)]

    store = pkgs.copy()
    assert try_sell(store, 500, 14) == [pkgA, (70, 17, 20220202)]
    assert store == [pkgD, pkgC, (30, 17, 20220202)]

    store = pkgs.copy()
    assert try_sell(store, 500, 15) == [pkgA, pkgB, pkgC]
    assert store == [pkgD]

    store = pkgs.copy()
    assert try_sell(store, 500, 16) == [pkgA, pkgB, pkgC, (2, 158, 20771023)]
    assert store == [(198, 158, 20771023)]

    store = pkgs.copy()
    assert try_sell(store, 500, 81) == [pkgA, pkgB, pkgC, pkgD]
    assert store == []

    store = pkgs.copy()
    assert try_sell(store, 500, 16) == [pkgA, pkgB, pkgC, (2, 158, 20771023)]
    assert store == [(198, 158, 20771023)]


if __name__ == '__main__':
    main()
