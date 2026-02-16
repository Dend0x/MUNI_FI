; Spočtěte Hammingovu vzdálenost slov uložených v ‹l1› a ‹l2›.
; Hammingovou vzdáleností je počet pozic, v nichž se vstupní slova
; liší hodnotou bitu. Výsledek uložte do ‹rv› a skočte na návěstí
; ‹check›. Hodnotu v registru ‹l7› neměňte.

main:
    ld   l7, data   → l1
    add  l7, 2      → l7
    ld   l7, data   → l2
    add  l7, 2      → l7
    eq   l1, 0xffff → t1 ; test-end marker
    jz   t1, solution
    halt

data: ;      l1       l2   →   rv
    .word  0xa1c4,  0xa1c4,     0
    .word  0xb3c4,  0xa1d5,     4
    .word  0xaa0a,  0x5055,    12
    .word  0x0f0f,  0xf0f0,    16
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
