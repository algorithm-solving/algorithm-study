from sys import stdin

read = stdin.readline

N = int(read())
heights = [0] + [int(read()) for _ in range(N)] + [0]
max_area = 0
indexes = [0]
for i, h in enumerate(heights):
    while h < heights[indexes[-1]]:
        height = heights[indexes.pop()]
        width = i - indexes[-1] - 1
        max_area = max(width * height, max_area)
    indexes.append(i)
print(max_area)
