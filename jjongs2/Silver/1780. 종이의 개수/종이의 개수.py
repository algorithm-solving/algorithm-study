from sys import stdin

read = stdin.readline


def divide_and_count(r, c, size):
    pivot = paper[r][c]
    if size == 1:
        counts[pivot] += 1
        return
    new_size = size // 3
    for dr in range(size):
        for dc in range(size):
            if paper[r + dr][c + dc] == pivot:
                continue
            for new_r in range(r, r + size, new_size):
                for new_c in range(c, c + size, new_size):
                    divide_and_count(new_r, new_c, new_size)
            return
    counts[pivot] += 1


N = int(read())
paper = [[int(n) for n in read().split()] for _ in range(N)]
counts = [0, 0, 0]
divide_and_count(0, 0, N)
for i in (-1, 0, 1):
    print(counts[i])
