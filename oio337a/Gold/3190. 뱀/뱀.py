def Solution():
    time = 0
    snake_arr = []
    direction = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    dir = 0
    nx, ny = 0, 0
    board[0][0] = 2
    snake_arr.append([0, 0])

    while True:
        time += 1
        nx += direction[dir][0]
        ny += direction[dir][1]
        if not 0 <= nx < N or not 0 <= ny < N:
            break

        if board[nx][ny] == 1:
            board[nx][ny] = 2
            snake_arr.append([nx, ny])
        elif board[nx][ny] == 0:
            board[nx][ny] = 2
            snake_arr.append([nx, ny])
            del_x, del_y = snake_arr.pop(0)
            board[del_x][del_y] = 0
        elif board[nx][ny] == 2:
            break

        if len(snake_dir) != 0 and time == snake_dir[0][0]:
            time, new_dir = snake_dir.pop(0)
            if new_dir == 'L':
                dir = (dir + 3) % 4
            elif new_dir == 'D':
                dir = (dir + 1) % 4

    return time


N = int(input())

board = [[0 for i in range(N)] for j in range(N)]

k = int(input())
apple_locs = []
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

l = int(input())
snake_dir = list(map(lambda x: [int(x[0]), str(x[1])], [
                 input().split() for _ in range(l)]))

print(Solution())
