from collections import deque
from sys import stdin

read = stdin.readline

MIN, MAX = 0, 10000


def D(n):
    return n * 2 if n < 5000 else n * 2 - MAX


def S(n):
    return n - 1 if n > MIN else MAX - 1


def L(n):
    return n * 10 - n // 1000 * 9999


def R(n):
    return n // 10 + n % 10 * 1000


def search(start, end):
    visited = ['' for _ in range(MAX)]
    visited[start] = '-'
    deq = deque([start])
    while True:
        n0 = deq.popleft()
        cmds = visited[n0]
        for func in (D, S, L, R):
            n = func(n0)
            if visited[n]:
                continue
            visited[n] = cmds + func.__name__
            if n == end:
                return visited[end][1:]
            deq.append(n)


results = []
case_count = int(read())
for _ in range(case_count):
    A, B = map(int, read().split())
    results.append(search(A, B))
print('\n'.join(results))
