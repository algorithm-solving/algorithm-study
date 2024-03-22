from collections import deque
from sys import stdin

read = stdin.readline

WHOLE = '12345678'


def search(start, end):
    depth = 0
    visited = {start}
    deq = deque([start])
    while deq:
        for _ in range(len(deq)):
            if (p1 := deq.popleft()) == end:
                return depth
            for first in range(N - K + 1):
                last = first + K - 1
                p = list(p1)
                for i in range(K // 2):
                    p[first + i], p[last - i] = p[last - i], p[first + i]
                if (p2 := ''.join(p)) in visited:
                    continue
                visited.add(p2)
                deq.append(p2)
        depth += 1
    return -1


N, K = map(int, read().split())
init = ''.join(read().split())
goal = WHOLE[:N]
print(search(init, goal))
