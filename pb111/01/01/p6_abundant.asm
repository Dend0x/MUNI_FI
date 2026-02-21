; Napište program, který rozhodne, je-li hodnota uložená v registru
; ‹l6› abundantním číslem (číslo ⟦n⟧ je abundantní, je-li součet
; všech jeho dělitelů ⟦d > 2n⟧). Vstup interpretujte jako číslo bez
; znaménka.
;
; Výsledek (1 pokud abundantní je, 0 jinak) uložte do registru ‹rv›
; a proveďte skok na návěstí ‹check›.  Hodnotu registru ‹l7› nijak
; neměňte.

main:
    ld   l7, data   → l6
    eq   l6, 0xffff → t1 ; test-end marker
    jz   t1, solution
    halt

data:   ; input, expect
    .word     1,      0
    .word    12,      1
    .word    17,      0
    .word    18,      1
    .word    24,      1
    .word    25,      0
    .word    -1,      0

check:
    add  l7, 2      → l7
    ld   l7, data   → t1
    eq   rv, t1     → t1
    asrt t1
    add  l7, 2      → l7
    jmp  main

.trigger set _tc_expect_ 6
.trigger inc _tc_

solution: ; zde začíná řešení
	put 1 -> l4
	put 2 -> l2
loop:
	udiv l6, l2 -> l3
	ugt l2, l3 -> l5
	jz l5, cont
	ugt l4, l6 -> rv
	jmp check
cont:
	umod l6, l2 -> l5
	jz l5, good
	add l2, 1 -> l2
	jmp loop
good:	
	add l4, l2 -> l4
	ugt l4, l6 -> l5
	jnz l5, done
	udiv l6, l2 -> l5
	eq l5, l2 -> l5
	jz l5, double
	add l2, 1 -> l2
	jmp loop
double:
	udiv l6, l2 -> l5
	add l4, l5 -> l4
	ugt l4, l6 -> l5
	jnz l5, done
	add l2, 1 -> l2
	jmp loop
done:
	put 1 -> rv
	jmp check