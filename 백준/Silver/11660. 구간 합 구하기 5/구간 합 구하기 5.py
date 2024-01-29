from itertools import product
from sys import stdin

N, M = map(int, stdin.readline().split())
table = [[0 for _ in range(N + 1)]] + [[0, *map(int, stdin.readline().split())] for _ in range(N)]
for r, c in product(range(1, N + 1), repeat=2):
    table[r][c] += table[r][c - 1] + table[r - 1][c] - table[r - 1][c - 1]
results = []
for line in stdin.read().splitlines():
    r1, c1, r2, c2 = map(int, line.split())
    r1, c1 = r1 - 1, c1 - 1
    results.append(table[r2][c2] - table[r2][c1] - table[r1][c2] + table[r1][c1])
print('\n'.join(map(str, results)))
