# 수리공 항승
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort()

cnt = 1
start = holes[0]
for i in range(1, N):
    if holes[i] - start + 1 > L:
        cnt += 1
        start = holes[i]

print(cnt)