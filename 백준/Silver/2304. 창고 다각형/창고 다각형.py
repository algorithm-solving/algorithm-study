from sys import stdin

read = stdin.readline

N = int(read())
pillars = sorted(tuple(map(int, read().split())) for _ in range(N))
min_area = 0
left_x, left_y = pillars[0]
for x, y in pillars:
    if y > left_y:
        min_area += (x - left_x) * left_y
        left_x, left_y = x, y
right_x, right_y = pillars[-1]
for x, y in reversed(pillars):
    if y > right_y:
        min_area += (right_x - x) * right_y
        right_x, right_y = x, y
min_area += (right_x - left_x + 1) * left_y
print(min_area)
