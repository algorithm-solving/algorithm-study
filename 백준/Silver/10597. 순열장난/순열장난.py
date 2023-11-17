from sys import stdin


def restore(i):
    if i >= L:
        return True
    for di in (1, 2):
        num = int(S[i:i + di])
        if not (0 < num <= N):
            continue
        if num in P:
            continue
        P.append(num)
        if restore(i + di):
            return True
        P.pop()
    return False


S = stdin.read().strip()
L = len(S)
N = (L + 9) // 2 if L > 9 else L
P = []
restore(0)
print(' '.join(map(str, P)))
