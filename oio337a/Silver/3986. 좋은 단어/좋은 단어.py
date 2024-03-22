import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for _ in range(n):
    s = input().rstrip()
    stack = []

    for i in range(len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])

    if not stack:
        cnt += 1
print(cnt)
