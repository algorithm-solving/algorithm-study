from sys import stdin

read = stdin.readline

pokedex = dict()
N, M = map(int, read().split())
for i in range(1, N + 1):
    index = str(i)
    name = read().strip()
    pokedex[index] = name
    pokedex[name] = index
results = []
for _ in range(M):
    question = read().strip()
    results.append(pokedex[question])
print('\n'.join(results))
