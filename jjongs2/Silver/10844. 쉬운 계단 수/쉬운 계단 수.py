from sys import stdin

read = stdin.readline

N = int(read())
counts = [[0] + [1 for _ in range(9)] for _ in range(N)]
for i in range(1, N):
    prev, curr = counts[i - 1], counts[i]
    curr[0] = prev[1]
    curr[9] = prev[8]
    for digit in range(1, 9):
        curr[digit] = prev[digit - 1] + prev[digit + 1]
print(sum(counts[-1]) % 1_000_000_000)
