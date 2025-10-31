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
    price = max_price - price_pkg
    amount_price_c = sum_price - max_price * sum_amount

    if price == 0:
        return amount_pkg if amount_price_c <= 0 else 0

    if price > 0:
        if amount_price_c <= 0:
            return amount_pkg
        minimum = (amount_price_c + price - 1) // price
        return amount_pkg if minimum <= amount_pkg else 0

    maximum = amount_price_c // price
    if maximum < 0:
        return 0
    return min(amount_pkg, maximum)


def try_sell(warehouse: list[Package],
             max_amount: int, max_price: int) -> list[Package]:

    # Tahle uloha me vnitrne boli

    result: list[Package] = []
    prices = set()
    amount = []
    best_kauf = -1
    total_amount = 0
    total_price = 0

    avg_price = 0
    actual_amount = 0

    for i in range(len(warehouse) - 1, -1, -1):
        if actual_amount <= max_amount:
            amount.append(i)
        pkg_amount, pkg_price, _ = warehouse[i]
        avg_price += pkg_amount * pkg_price
        actual_amount += pkg_amount
        if avg_price <= max_price * actual_amount:
            prices.add(i)
            if i - 1 >= 0:
                prices.add(i - 1)

    best_left = 0
    best_total_sold = 0

    for i in range(len(amount) - 1, -1, -1):
        edge = amount[i]
        inner_total_amount = 0
        inner_total_price = 0

        for j in range(len(warehouse) - 1, edge, -1):
            pkg_amount, pkg_price, _ = warehouse[j]
            inner_total_amount += pkg_amount
            inner_total_price += pkg_amount * pkg_price

        total_sold = 0
        left_to_do = 0

        if inner_total_amount >= max_amount:
            total_sold = max_amount
        else:
            pkg_amount, pkg_price, _ = warehouse[edge]
            left_to_do = find_max_sell_price(pkg_amount,
                                             inner_total_price, pkg_price,
                                             max_price, inner_total_amount)
            left_to_do = min(left_to_do, max_amount - inner_total_amount)
            total_sold = inner_total_amount + left_to_do

        pkg_amount, pkg_price, _ = warehouse[edge]

        if total_sold > 0:
            good_price = inner_total_price + left_to_do * pkg_price
            good_amount = inner_total_amount + left_to_do
            if (
                good_price <= max_price * good_amount
                and total_sold > best_total_sold
            ):
                best_total_sold = total_sold
                best_kauf = edge
                best_left = left_to_do

    if best_kauf == -1 or best_total_sold == 0:
        return result

    for i in range(len(warehouse) - 1, best_kauf, -1):
        pkg_amount, pkg_price, ex = warehouse.pop()
        total_amount += pkg_amount
        total_price += pkg_amount * pkg_price
        result.append((pkg_amount, pkg_price, ex))

    _, best_pkg_price, ex = warehouse[best_kauf]

    if best_left > 0:
        result.append((best_left, best_pkg_price, ex))
        to_pop_amount, to_pop_price, to_pop_ex = warehouse.pop()
        to_pop_amount -= best_left
        if to_pop_amount > 0:
            warehouse.append((to_pop_amount, to_pop_price, to_pop_ex))
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
