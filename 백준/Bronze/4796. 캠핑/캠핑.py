from sys import stdin

read = stdin.readline

results = []
i = 1
while True:
    L, P, V = map(int, read().split())
    if L == 0:
        break
    result = L * (V // P) + min(L, V % P)
    results.append(f'Case {i}: {result}')
    i += 1
print('\n'.join(results))
