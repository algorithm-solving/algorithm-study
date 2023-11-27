from sys import stdin

DIGIT_COUNT = 10
DIVISOR = 1_000_000_000
MASK_COUNT = 1 << DIGIT_COUNT


def update(p, c, mask):
    for m0 in range(MASK_COUNT):
        m = m0 | mask
        c[m] = (c[m] + p[m0]) % DIVISOR


def count(length):
    if length < DIGIT_COUNT:
        return 0
    prev = [[0 for _ in range(MASK_COUNT)] for _ in range(DIGIT_COUNT)]
    for d in range(1, 10):
        prev[d][1 << d] = 1
    for _ in range(length - 1):
        curr = [[0 for _ in range(MASK_COUNT)] for _ in range(DIGIT_COUNT)]
        update(prev[1], curr[0], 1 << 0)
        update(prev[8], curr[9], 1 << 9)
        for d in range(1, 9):
            c, mask = curr[d], 1 << d
            update(prev[d - 1], c, mask)
            update(prev[d + 1], c, mask)
        prev = curr
    return sum(c[-1] for c in curr) % DIVISOR


N = int(stdin.read())
print(count(N))
