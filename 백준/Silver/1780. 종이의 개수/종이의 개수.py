import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def solution(i, j, d):
    color = board[i][j]
    for it in range(i, i+d):
        for jt in range(j, j+d):
            if color != board[it][jt]:
                newd = d//3
                for mi in range(0, 3):
                    for mj in range(0, 3):
                        solution(i + mi * newd, j + mj * newd, newd)
                return
    result[color] += 1


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
result = [0, 0, 0]
solution(0, 0, n)
for i in range(-1, 2):
    print(result[i])
