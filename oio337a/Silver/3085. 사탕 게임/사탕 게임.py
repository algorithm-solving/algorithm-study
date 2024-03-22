import sys
input = sys.stdin.readline

n = int(input())
pan = [list(input()) for _ in range(n)]
answer = 0

# 가장 긴 인접한 연속된 색 확인


def check(board):
    cnt = 0
    for i in range(n):
        cnt_r = 1
        cnt_c = 1
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                cnt_r += 1
            else:
                cnt = max(cnt, cnt_r)
                cnt_r = 1

            if board[j][i] == board[j+1][i]:
                cnt_c += 1
            else:
                cnt = max(cnt, cnt_c)
                cnt_c = 1
        cnt = max(cnt, cnt_r, cnt_c)
    return cnt


# 다르면 위치바꾸기 행, 열
for i in range(n):
    for j in range(n-1):
        # 다르다면 위치 바꾸기 행
        if pan[i][j] != pan[i][j+1]:
            temp = pan[i][j]
            pan[i][j] = pan[i][j+1]
            pan[i][j+1] = temp

            answer = max(answer, check(pan))
            # 바꾼거 되돌리기
            temp = pan[i][j]
            pan[i][j] = pan[i][j+1]
            pan[i][j+1] = temp
        # 다르다면 위치 바꾸기 열
        if pan[j][i] != pan[j+1][i]:
            temp = pan[j][i]
            pan[j][i] = pan[j+1][i]
            pan[j+1][i] = temp

            answer = max(answer, check(pan))
            # 바꾼거 되돌리기
            temp = pan[j][i]
            pan[j][i] = pan[j+1][i]
            pan[j+1][i] = temp
print(answer)
