from sys import stdin

read = stdin.readline

n = int(read())
curr = 1
prev = 1
for _ in range(n - 1):
    curr, prev = (curr + prev * 2) % 10007, curr
print(curr)
