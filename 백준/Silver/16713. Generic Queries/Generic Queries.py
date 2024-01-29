from sys import stdin

read = stdin.readline

N, Q = map(int, read().split())
a = [0, *map(int, read().split())]
for i in range(2, N + 1):
    a[i] ^= a[i - 1]
result = 0
for _ in range(Q):
    s, e = map(int, read().split())
    result ^= a[e] ^ a[s - 1]
print(result)
