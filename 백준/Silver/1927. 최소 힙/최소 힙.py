from heapq import heappop
from heapq import heappush
from sys import stdin

_ = stdin.readline()
results = []
nums = []
for x in map(int, stdin.read().splitlines()):
    if x > 0:
        heappush(nums, x)
    elif x == 0:
        results.append(heappop(nums) if nums else 0)
print('\n'.join(map(str, results)))
