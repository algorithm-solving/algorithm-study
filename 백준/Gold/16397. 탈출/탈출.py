from collections import deque
from math import log10
from sys import stdin

MAX = 99_999

N, T, G = map(int, stdin.read().split())
counts = [-1 for _ in range(MAX + 1)]
counts[N] = 0
deq = deque([N])
while deq:
    if (n0 := deq.popleft()) == G:
        break
    nums = []
    if n0 < MAX:
        nums.append(n0 + 1)
    if n0 > 0 and (n := n0 * 2) <= MAX:
        nums.append(n - 10 ** int(log10(n)))
    for n in nums:
        if counts[n] < 0 and counts[n0] < T:
            counts[n] = counts[n0] + 1
            deq.append(n)
count = counts[G]
print(count if count >= 0 else 'ANG')
