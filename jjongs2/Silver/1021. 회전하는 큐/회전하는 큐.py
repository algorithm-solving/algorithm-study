from sys import stdin

read = stdin.readline

N, M = map(int, read().split())
targets = tuple(map(int, read().split()))
nums = list(range(1, N + 1))
count = 0
for i, t in enumerate(targets):
    index = nums.index(t)
    count += min(index, N - i - index)
    nums = nums[index + 1:] + nums[:index]
print(count)
