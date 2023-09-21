from math import inf
from sys import stdin

read = stdin.readline

L, N, r_F, r_B = map(int, read().split())
coeff = r_F - r_B
stops = [(0, inf)]
for _ in range(N):
    x, c = map(int, read().split())
    while stops[-1][1] <= c:
        stops.pop()
    stops.append((x, c))
score = sum(stops[i][1] * (stops[i][0] - stops[i - 1][0]) for i in range(1, len(stops)))
print(coeff * score)
