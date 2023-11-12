from sys import stdin

F, S, G, U, D = map(int, stdin.readline().split())
counts = [-1 for _ in range(F + 1)]
counts[S] = 0
deq = [S]
while deq:
    if (f0 := deq.pop(0)) == G:
        break
    if (f := f0 + U) <= F and counts[f] < 0:
        counts[f] = counts[f0] + 1
        deq.append(f)
    if (f := f0 - D) > 0 and counts[f] < 0:
        counts[f] = counts[f0] + 1
        deq.append(f)
count = counts[G]
print(count if count >= 0 else 'use the stairs')
