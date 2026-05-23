def combinator(n: int, k: int) -> int:
    if k == 0:
        return 1
    if n == k:
        return 1
    return combinator(n - 1, k - 1) + combinator(n - 1, k)

sex = { 0: "a", 1: "b", 2: "c" }

def perms(count: int, n: int, used: set[int], perms_i: set[int], text: str) -> None:
    if count == 0:
        perms_i.add(text)
        return

    for i in range(n):
        if i not in used:
            used.add(i)
            perms(count - 1, n, used, perms_i, text + sex.get(i))
            used.remove(i)

def perm(n: int):
    used = set()
    perms_i = set()
    perms(n, n, used, perms_i, "")
    print(perms_i)

perm(3)