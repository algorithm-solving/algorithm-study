from sys import stdin


def find_value(i):
    if not A.get(i):
        A[i] = find_value(i // P) + find_value(i // Q)
    return A[i]


A = {0: 1}
N, P, Q = map(int, stdin.read().split())
print(find_value(N))
