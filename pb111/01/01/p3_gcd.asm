; Vaším úkolem je naprogramovat Euklidův algoritmus pro nalezení
; největšího společného dělitele hodnot uložených v registrech ‹l1›
; a ‹l2› – obě hodnoty interpretujte jako 16bitová celá čísla bez
; znaménka.
;
; Výsledek uložte do registru ‹rv›. Po ukončení výpočtu skočte na
; návěstí ‹check›. Hodnotu registru ‹l7› neměňte.

main:
    ld   l7, data   → l1
    add  l7, 2      → l7
    ld   l7, data   → l2
    add  l7, 2      → l7
    eq   l1, 0xffff → t1 ; test-end marker
    jz   t1, solution
    halt

data:   ; gcd l1,    l2  →  rv
    .word       1,    1,     1
    .word       2,    2,     2
    .word      18,   15,     3
    .word      20,   30,    10
    .word      -1,    0

check:
    ld   l7, data   → t1
    eq   rv, t1     → t1
    asrt t1
    add  l7, 2      → l7
    jmp  main

.trigger set _tc_expect_ 4
.trigger inc _tc_

solution: ; zde začíná řešení
	ult l1, l2 -> l3
	jz l3, gcd
	copy l1 -> l3
	copy l2 -> l1
	copy l3 -> l2
gcd:
	jz l2, end
	umod l1, l2 -> l3
	copy l2 -> l1
	copy l3 -> l2
	jmp gcd
end:
	copy l1 -> rv
	jmp check