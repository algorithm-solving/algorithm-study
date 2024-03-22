from sys import stdin

A = ord('A')
DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))

max_count = 0
R, C = map(int, stdin.readline().split())
visited = [[0 for _ in range(C)] for _ in range(R)]
board = [[1 << ord(char) - A for char in line] for line in stdin.read().split()]
stack = [((0, 0), 1, board[0][0])]
while stack:
    (r0, c0), count, path = stack.pop()
    max_count = max(max_count, count)
    for dr, dc in DIRECTIONS:
        r, c = r0 + dr, c0 + dc
        if not (0 <= r < R and 0 <= c < C):
            continue
        letter = board[r][c]
        if letter & path != 0:
            continue
        new_path = path | letter
        if new_path == visited[r][c]:
            continue
        visited[r][c] = new_path
        stack.append(((r, c), count + 1, new_path))
print(max_count)
