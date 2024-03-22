from sys import stdin

read = stdin.readline

N = int(read())
A = list(map(int, read().split()))
sums = A[:]
for end in range(1, N):
    for i in range(end):
        if A[i] < A[end]:
            sums[end] = max(sums[end], sums[i] + A[end])
print(max(sums))
