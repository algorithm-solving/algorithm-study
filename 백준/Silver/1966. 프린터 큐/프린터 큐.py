from heapq import heapify
from heapq import heappop
from heapq import heapreplace
from sys import stdin

read = stdin.readline

results = []
case_count = int(read())
for _ in range(case_count):
    N, M = map(int, read().split())
    priorities = [(-int(p), i) for i, p in enumerate(read().split())]
    heapify(priorities)
    popped_p, popped_i = 0, 0
    while True:
        p, i = priorities[0]
        if p > popped_p and i < popped_i:
            heapreplace(priorities, (p, i + N))
            continue
        popped_p, popped_i = heappop(priorities)
        if popped_i % N == M:
            break
    results.append(N - len(priorities))
print('\n'.join(map(str, results)))
