; Vaším úkolem bude otočit pořadí bitů ve slově. Vstupní slovo bude
; uloženo v registru ‹l1›, výsledek uložte do ‹rv› a skočte na návěstí
; ‹check›. Hodnotu v registru ‹l7› neměňte.

main:
    ld   l7, data   → l1
    add  l7, 2      → l7
    eq   l1, 0xffff → t1 ; test-end marker
    jz   t1, solution
    halt

data: ;      l1   →   rv
    .word  0x0001,  0x8000
    .word  0xfffe,  0x7fff
    .word  0x1248,  0x1248
    .word  0x37a9,  0x95ec
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
