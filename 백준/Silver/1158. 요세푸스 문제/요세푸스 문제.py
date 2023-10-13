from sys import stdin

read = stdin.readline

N, K = map(int, read().split())
nums = list(range(1, N + 1))
executed = []
index = 0
for i in range(N):
    index = (index + K - 1) % (N - i)
    executed.append(nums.pop(index))
print(f"<{', '.join(map(str, executed))}>")
