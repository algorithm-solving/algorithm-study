from sys import stdin

read = stdin.readline

N, S = map(int, read().split())
nums = map(int, read().split())
sums = [0]
for n in nums:
    sums.extend([n + s for s in sums])
del sums[0]
print(sums.count(S))
