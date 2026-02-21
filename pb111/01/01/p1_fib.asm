; Matematická funkce ‹fib› počítá ‹n›-tý prvek tzv. Fibonacciho
; posloupnosti, dané předpisem: ⟦f(1) = f(2) = 1, f(n) = f(n - 1) +
; f(n - 2)⟧. Každý prvek této posloupnosti je tedy součtem
; předchozích dvou (s výjimkou prvních dvou, které jsou pevně dané).

; Vaším úkolem je naprogramovat iterativní výpočet ⟦n⟧-tého
; Fibonacciho čísla. Vstupní hodnotu ⟦n⟧ naleznete v registru ‹l6›,
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
	sle l6, 0 -> l1
	jz l1, gre_0
	put 0 -> rv
	jmp check
gre_0:
	eq l6, 1 -> l1
	jz l1, val_ok
	put 1 -> rv
	jmp check
val_ok:
	put 1 -> l1
	put 1 -> l2
	sub l6, 2 -> l6
loop:
	jz l6, end
	sub l6, 1 -> l6
	copy l2 -> l3
	add l1, l2 -> l2
	copy l3 -> l1
	jmp loop
end:
	copy l2 -> rv
	jmp check