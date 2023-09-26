from sys import stdin

read = stdin.readline

Z = ((0, 1), (2, 3))


def find_order(r, c, size):
    if size == 0:
        return 0
    return Z[r & 1][c & 1] + 4 * find_order(r >> 1, c >> 1, size - 1)


N, r, c = map(int, read().split())
print(find_order(r, c, N))
