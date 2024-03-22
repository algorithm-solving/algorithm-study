from sys import stdin

read = stdin.readline

x, y, z = map(int, read().split())
N = int(read())
cubes = [tuple(map(int, read().split())) for _ in range(N)]
total_count = 0
occupied = 0
prev_A = cubes[-1][0]
for A, B in reversed(cubes):
    occupied <<= 3 * (prev_A - A)
    maximum = (x >> A) * (y >> A) * (z >> A)
    count = min(B, maximum - occupied)
    total_count += count
    occupied += count
    prev_A = A
print(total_count if occupied == x * y * z else -1)
