; Mnohé procesory nabízí tzv. vektorové instrukce, které se
; k jednomu velkému registru chovají, jako by obsahoval několik
; menších čísel uložených vedle sebe. Vaším úkolem bude emulovat
; jednu z těchto instrukcí; konkrétně sčítání, které 16bitové
; registry považuje za dvojice dvou osmibitových čísel a dvě takové
; dvojice sečte po složkách. Vstup je v registrech ‹l1› a ‹l2›,
; výsledek uložte do ‹rv› (opět jako 2 osmibitové hodnoty) a skočte
; na návěstí ‹check›. Hodnotu v registru ‹l7› neměňte.

main:
    ld   l7, data   → l1
    add  l7, 2      → l7
    ld   l7, data   → l2
    add  l7, 2      → l7
    eq   l1, 0xffff → t1 ; test-end marker
    jz   t1, solution
    halt

data: ;      l1   +   l2   →   rv
    .word  0x0101,  0x0f0f,  0x1010
    .word  0x00ff,  0x0010,  0x000f
    .word  0x0002,  0xfffe,  0xff00
    .word  0xaea9,  0x6188,  0x0f31
    .word      -1,       0

check:
    ld   l7, data   → t1
    eq   rv, t1     → t1
    asrt t1
    add  l7, 2      → l7
    jmp  main

.trigger set _tc_expect_ 4
.trigger inc _tc_


solution: ; zde začíná řešení
