from itertools import combinations_with_replacement
from sys import stdin

read = stdin.readline

triangle_nums = [n * (n + 1) // 2 for n in range(1, 46)]
combs = combinations_with_replacement(triangle_nums, 3)
triangle_sums = set(sum(c) for c in combs)
T = int(read())
result = ['1' if int(read()) in triangle_sums else '0' for _ in range(T)]
print('\n'.join(result))
