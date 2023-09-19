from sys import stdin

read = stdin.readline

N, M = map(int, read().split())
board = tuple(read().strip() for _ in range(N))
chess_board = ('WB' * 4, 'BW' * 4) * 4
min_count = 64
for r in range(N - 7):
    for c in range(M - 7):
        count = 0
        for dr in range(8):
            for dc in range(8):
                if board[r + dr][c + dc] != chess_board[dr][dc]:
                    count += 1
        min_count = min(count, 64 - count, min_count)
print(min_count)
