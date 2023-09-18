from sys import stdin
from itertools import combinations

read = stdin.readline

heights = [int(read()) for _ in range(9)]
combs = combinations(heights, 7)
result = next(c for c in combs if sum(c) == 100)
print(*sorted(result), sep='\n')
