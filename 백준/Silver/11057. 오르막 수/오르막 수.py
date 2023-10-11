from math import comb
from sys import stdin

read = stdin.readline

N = int(read())
print(comb(9 + N, N) % 10007)
