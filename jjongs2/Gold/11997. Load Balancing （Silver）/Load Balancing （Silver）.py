from itertools import product
from sys import stdin


def balance(r, c):
    top_left = prefix_sums[r][c]
    top_right = prefix_sums[r][max_c] - top_left
    bottom_left = prefix_sums[max_r][c] - top_left
    bottom_right = prefix_sums[max_r][max_c] - bottom_left - top_right - top_left
    return max(bottom_right, bottom_left, top_right, top_left)


def compress(tgt, index):
    tgt.sort(key=lambda x: x[index])
    comp_value, prev = 1, tgt[0][index]
    for elem in tgt:
        if prev < elem[index]:
            prev = elem[index]
            comp_value += 1
        elem[index] = comp_value
    return comp_value


N = int(stdin.readline())
locations = [list(map(int, line.split())) for line in stdin.read().splitlines()]
max_r = compress(locations, 0)
max_c = compress(locations, 1)
prefix_sums = [[0 for _ in range(max_c + 1)] for _ in range(max_r + 1)]
for r, c in locations:
    prefix_sums[r][c] = 1
for r, c in product(range(1, max_r + 1), range(1, max_c + 1)):
    prefix_sums[r][c] += prefix_sums[r][c - 1] + prefix_sums[r - 1][c] - prefix_sums[r - 1][c - 1]
result = N
for r, c in product(range(max_r), range(max_c)):
    result = min(result, balance(r, c))
print(result)
