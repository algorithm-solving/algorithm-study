# 히스토그램

import sys
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
result = 0
s = []

for i in range(n):
    while s and data[s[-1]] > data[i]:
        height = data[s[-1]]
        s.pop()
        width = i
        if s:
            width = (i - s[-1] - 1)
        result = max(result, width * height)
    s.append(i)

while s:
    height = data[s[-1]]
    s.pop()
    width = n
    if s:
        width = (n - s[-1] - 1)
    result = max(result, width * height)

print(result)