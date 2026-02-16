; Uvažme následující funkci ‹f› na kladných celých číslech:
;
;       f(n) = n / 2     je-li n sudé
;       f(n) = 3n +1     je-li n liché
;
; Collatzova domněnka říká, že budeme-li na libovolné kladné celé
; číslo tuto funkci opakovaně aplikovat, dostaneme se nakonec
; k výsledku 1.
;
; Vaším úkolem je tento výpočet provést a
;
;   1. spočítat, po kolika aplikacích funkce ‹f› na vstup je poprvé
;      výsledkem jednička a
;   2. zjistit nejvyšší mezivýsledek, který při výpočtu vznikl.
;
; Můžete předpokládat, že pro číslo na vstupu domněnka skutečně platí
; a že v průběhu výpočtu nevznikne mezivýsledek, který by se nevlezl
; do šestnáctibitového registru.
;
; Počáteční číslo naleznete v registru ‹l1›. Počet aplikací funkce
; uložte do ‹rv›, nalezené maximum do ‹l6› a skočte na návěstí
; ‹check›. Hodnotu v registru ‹l7› neměňte.

main:
    ld   l7, data   → l1
    add  l7, 2      → l7
    eq   l1, 0xffff → t1 ; test-end marker
    jz   t1, solution
    halt

data: ;    l1  →  rv  l6
    .word   1,     0,    1
    .word   8,     3,    8
    .word  25,    23,   88
    .word  27,   111, 9232
    .word  -1,     0

check:
    ld   l7, data   → t1
    eq   rv, t1     → t1
    asrt t1
    add  l7, 2      → l7
    ld   l7, data   → t1
    eq   l6, t1     → t1
    asrt t1
    add  l7, 2      → l7
    jmp  main

.trigger set _tc_expect_ 4
.trigger inc _tc_

solution: ; zde začíná řešení
