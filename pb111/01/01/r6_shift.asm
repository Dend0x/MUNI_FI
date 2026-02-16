; Proveďte levý bitový posuv:
;
;  • každý bit se posune o jednu pozici doleva,
;  • pracujeme na bitech v registru ‹rv›,
;  • na pozicích zadaných registry ‹l2› a ‹l3› (‹l2› je index
;    nejnižšího, ‹l3› index nejvyššího bitu).
;
; Rotaci provádějte na místě (v registru ‹rv›) a pouze na vymezených
; bitech, poté skočte na návěstí ‹check›. Hodnotu v registru ‹l7›
; neměňte. Můžete předpokládat, že indexy bitů budou v rozsahu 0–15.
; Nula označuje nejméně významný bit slova.

main:
    ld   l7, data   → rv
    add  l7, 2      → l7
    ld   l7, data   → l2
    add  l7, 2      → l7
    ld   l7, data   → l3
    add  l7, 2      → l7
    eq   rv, 0xffff → t1 ; test-end marker
    jz   t1, solution
    halt

data: ;      rv     l2   l3  →   rv
    .word  0x1000,   0,  15,   0x2000
    .word  0xff00,   0,  15,   0xfe00
    .word  0xfe00,   8,  15,   0xfc00
    .word  0xaaaa,   8,  15,   0x54aa
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

