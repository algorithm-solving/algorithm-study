
def counting_star(n):
    global board

    if n == 3:
        board[0][:3] = board[2][:3] = ['*']*3
        board[1][:3] = ['*', ' ', '*']
        return

    a = n // 3
    counting_star(a)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                board[a*i+k][a*j:a*(j+1)] = board[k][:a]


N = int(input())
board = [[' ' for i in range(N)] for i in range(N)]
counting_star(N)

for i in board:
    print(*i, sep='')
