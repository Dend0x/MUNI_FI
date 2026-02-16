; Prohoďte dva zadané bity ve slově v registru ‹l1›. Indexy bitů
; jsou v ‹l2› a ‹l3›. Můžete předpokládat, že budou v rozsahu 0–15,
; nula označuje nejméně významný bit slova. Výsledek uložte do ‹rv›
; a skočte na návěstí ‹check›. Hodnotu v registru ‹l7› neměňte.

main:
    ld   l7, data   → l1
    add  l7, 2      → l7
    ld   l7, data   → l2
    add  l7, 2      → l7
    ld   l7, data   → l3
    add  l7, 2      → l7
    eq   l1, 0xffff → t1 ; test-end marker
    jz   t1, solution
    halt

data: ;      l1     l2   l3  →   rv
    .word  0xabcd,   5,   5,   0xabcd
    .word  0xff00,   7,   8,   0xfe80
    .word  0xff00,   8,   7,   0xfe80
    .word  0x869e,   0,  15,   0x069f
    .word      -1,   0

check:
    ld   l7, data   → t1
    eq   rv, t1     → t1
    asrt t1
    add  l7, 2      → l7
    jmp  main

.trigger set _tc_expect_ 4
.trigger inc _tc_

solution: ; zde začíná řešení
