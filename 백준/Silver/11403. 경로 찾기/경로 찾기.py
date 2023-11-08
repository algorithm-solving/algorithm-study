from itertools import product
from sys import stdin

N = int(stdin.readline())
adj = [line.split() for line in stdin.read().splitlines()]
for via, v1, v2 in product(range(N), repeat=3):
    if adj[v1][via] == '1' and adj[via][v2] == '1':
        adj[v1][v2] = '1'
print('\n'.join(' '.join(row) for row in adj))
