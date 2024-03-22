from collections import deque
from sys import stdin

ANSWER = 123456789
BLANK = '9'
DIRECTIONS = (-3, -1, 1, 3)


def search(start, end):
    if start == end:
        return 0
    d0 = int(BLANK)
    count = 0
    visited = {start}
    deq = deque([start])
    while deq:
        count += 1
        for _ in range(len(deq)):
            p0 = deq.popleft()
            p0_str = str(p0)
            i0 = 8 - p0_str.index(BLANK)
            for di in DIRECTIONS:
                i = i0 + di
                if not (0 <= i < 9):
                    continue
                if i // 3 == i0 // 3 or i % 3 == i0 % 3:
                    d = int(p0_str[8 - i])
                    p = p0 + (d0 - d) * pow(10, i) + (d - d0) * pow(10, i0)
                    if p == end:
                        return count
                    if p in visited:
                        continue
                    visited.add(p)
                    deq.append(p)
    return -1


puzzle = ''.join(stdin.read().split())
num = int(puzzle.replace('0', BLANK))
print(search(num, ANSWER))
