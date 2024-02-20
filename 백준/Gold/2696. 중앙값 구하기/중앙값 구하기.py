from heapq import heappush
from heapq import heappushpop
from sys import stdin

read = stdin.readline


def find_medians(seq):
    max_heap, min_heap = [], []
    median = nums.pop(0)
    medians = [median]
    for i, n in enumerate(seq):
        if i & 1 == 0:
            bigger, smaller = max(n, median), min(n, median)
            heappush(max_heap, -smaller)
            heappush(min_heap, bigger)
            continue
        if n > min_heap[0]:
            median = heappushpop(min_heap, n)
        else:
            median = -heappushpop(max_heap, -n)
        medians.append(median)
    return medians


results = []
T = int(read())
for _ in range(T):
    nums = []
    M = int(read())
    for _ in range(M // 10 + 1):
        for num in map(int, read().split()):
            nums.append(num)
    results.append(str(M // 2 + 1))
    medians = find_medians(nums)
    for i in range(0, len(medians), 10):
        line = ' '.join(map(str, medians[i:i + 10]))
        results.append(line)
print('\n'.join(results))
