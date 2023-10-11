from math import comb
from sys import stdin

read = stdin.readline

N, K = map(int, read().split())
print(comb(N, K) % 10007)
