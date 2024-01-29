from sys import stdin

read = stdin.readline

results = []
T = int(read())
for _ in range(T):
    N = int(read())
    X = list(map(int, read().split()))
    for i in range(1, N):
        X[i] += max(0, X[i - 1])
    results.append(max(X))
print('\n'.join(map(str, results)))
