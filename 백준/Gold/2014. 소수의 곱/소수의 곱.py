from heapq import heappop
from heapq import heappush
from sys import stdin

read = stdin.readline

_, N = map(int, read().split())
prime_nums = list(map(int, read().split()))
products = []
for prime in prime_nums:
    heappush(products, prime)
for _ in range(N - 1):
    popped = heappop(products)
    for prime in prime_nums:
        heappush(products, prime * popped)
        if popped % prime == 0:
            break
print(products[0])
