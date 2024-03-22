from sys import stdin

read = stdin.readline

S = read().strip()
N = int(read())
words = tuple(read().strip() for _ in range(N))
results = [1] + [0 for _ in range(len(S))]
for start, result in enumerate(results):
    if result == 0:
        continue
    for word in words:
        if S.startswith(word, start):
            results[start + len(word)] = 1
print(results[-1])
