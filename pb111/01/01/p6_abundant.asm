find_depth:
	call find_depth_rec
	ret

find_depth_rec:
	jnz rv, not_empty
	put 0 -> l6
	ret
not_empty:
	push rv
	call get_children
	copy l1 -> rv
	push l2
	call find_depth_rec
	copy l6 -> l4
	pop l2
	copy l2 -> rv
	call find_depth_rec
	copy l6 -> l5
	sgt l4, l5 -> l3
	jz l3, second
	add l4, 1 -> l4
	push l4
	pop rv
	ret
second:
	add l5, 1 -> l5
	push l5
	pop rv
	ret