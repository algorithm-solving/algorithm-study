from sys import stdin

read = stdin.readline

count = 0
N = int(read())
for _ in range(N):
    stack = []
    word = read().strip()
    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    if not stack:
        count += 1
print(count)
