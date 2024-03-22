# 외계인의 기타 연주

import sys
input = sys.stdin.readline

N, P = map(int, input().split())
cnt = 0
lst = [[] for _ in range(7)]

for i in range(N):
    n, p = map(int, input().split())
    if not lst[n-1]:
        lst[n-1].append(p)
        cnt += 1
    else:
        while lst[n-1] and p < lst[n-1][-1]:
            lst[n-1].pop()
            cnt += 1
        if not lst[n-1] or p > lst[n-1][-1]:
            lst[n-1].append(p)
            cnt += 1
        else:
            pass
print(cnt)