N = int(input())
li = []

for i in range(N):
    start, end = map(int, input().split())
    li.append([start, end])

li = sorted(li, key=lambda x: x[0])
li = sorted(li, key=lambda x: x[1])

last = 0
cnt = 0
for i, k in li:
    if i >= last:
        cnt += 1
        last = k

print(cnt)
