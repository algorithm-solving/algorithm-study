from sys import stdin


def search(r, max_c):
    if r == N:
        return 1
    count = 0
    for c in range(max_c):
        d1, d2 = r - c, r + c
        if cols[c] or diags1[d1] or diags2[d2]:
            continue
        cols[c] = diags1[d1] = diags2[d2] = True
        count += search(r + 1, N)
        cols[c] = diags1[d1] = diags2[d2] = False
    return count


N = int(stdin.read())
cols = [False for _ in range(N)]
diags1 = [False for _ in range(2 * N - 1)]
diags2 = diags1.copy()
result = search(0, N // 2) * 2
if N & 1 == 1:
    i = N // 2
    cols[i] = diags1[-i] = diags2[i] = True
    result += search(1, N)
print(result)
