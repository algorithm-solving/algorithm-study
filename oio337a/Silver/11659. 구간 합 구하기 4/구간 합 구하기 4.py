import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))

prefix = [0] + [li[0]]

for i in range(1, n):  # 누적합
    prefix.append(prefix[-1] + li[i])
for _ in range(m):
    s, e = map(int, input().split())
    if s == 1:
        print(prefix[e])
    elif s == e:
        print(li[e - 1])
    else:
        print(prefix[e]-prefix[s - 1])
