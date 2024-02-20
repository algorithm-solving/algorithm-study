from heapq import heappop
from heapq import heappush
from sys import stdin

_ = stdin.readline()
results = []
nums = []
for x in map(int, stdin.read().splitlines()):
    if x == 0:
        results.append(heappop(nums)[1] if nums else 0)
    else:
        heappush(nums, (abs(x), x))
print('\n'.join(map(str, results)))
