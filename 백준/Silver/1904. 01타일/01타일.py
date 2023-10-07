from sys import stdin

read = stdin.readline

N = int(read())
curr = 1
prev = 1
for _ in range(N - 1):
    curr, prev = curr + prev, curr
    if curr >= 15746:
        curr -= 15746
print(curr)
