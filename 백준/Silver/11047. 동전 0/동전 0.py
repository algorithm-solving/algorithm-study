N, K = map(int, input().split())

li = []
cnt = 0
for i in range(N):
    li.append(int(input()))

li.sort(reverse=True)

for i in li:
    if K >= i:
        cnt += K // i
        K -= (K//i)*i

print(cnt)
