from collections import deque
from enum import Enum
from sys import stdin

read = stdin.readline

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


class Object(Enum):
    NOTHING = 0
    APPLE = 1
    SNAKE = 2


def play_game(board_size, board, turns):
    snake = deque([(0, 0)])
    r, c = 0, 0
    way = 0
    time = 0
    while True:
        time += 1
        dr, dc = DIRECTIONS[way]
        r, c = r + dr, c + dc
        if not (0 <= r < board_size and 0 <= c < board_size):
            return time
        state = board[r][c]
        if state == Object.SNAKE:
            return time
        if state != Object.APPLE:
            tail_r, tail_c = snake.pop()
            board[tail_r][tail_c] = Object.NOTHING
        snake.appendleft((r, c))
        board[r][c] = Object.SNAKE
        if turns and time == int(turns[0][0]):
            _, direction = turns.popleft()
            way = (way - 1) % 4 if direction == 'L' else (way + 1) % 4


N = int(read())
K = int(read())
board = [[Object.NOTHING for _ in range(N)] for _ in range(N)]
board[0][0] = Object.SNAKE
for _ in range(K):
    r, c = map(int, read().split())
    board[r - 1][c - 1] = Object.APPLE
L = int(read())
turns = deque(read().split() for _ in range(L))
print(play_game(N, board, turns))
