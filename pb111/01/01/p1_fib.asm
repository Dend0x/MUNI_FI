; Matematická funkce ‹fib› počítá ‹n›-tý prvek tzv. Fibonacciho
; posloupnosti, dané předpisem: ⟦f(1) = f(2) = 1, f(n) = f(n - 1) +
; f(n - 2)⟧. Každý prvek této posloupnosti je tedy součtem
; předchozích dvou (s výjimkou prvních dvou, které jsou pevně dané).

; Vaším úkolem je naprogramovat iterativní výpočet ⟦n⟧-tého
; Fibonacciho čísla. Vstupní hodnotu ⟦n⟧ naleznete v registru ‹l6›,
; výsledek uložte do registru ‹rv›. Po skončení výpočtu proveďte
; skok na návěstí ‹check›. Hodnotu registru ‹l7› zachovejte.

main:
    ld   l7, data   → l6
    eq   l6, 0xffff → t1 ; test-end marker
    jz   t1, solution
    halt

data:   ; input, expect
    .word     1,      1
    .word     9,     34
    .word    11,     89
    .word    20,   6765
    .word    -1,      0

check:
    add  l7, 2      → l7
    ld   l7, data   → t1
    eq   rv, t1     → t1
    asrt t1
    add  l7, 2      → l7
    jmp  main

.trigger set _tc_expect_ 4
.trigger inc _tc_

solution: ; zde začíná řešení
