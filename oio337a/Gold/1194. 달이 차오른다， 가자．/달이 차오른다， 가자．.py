from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]
visit = [[-1]*m for _ in range(n)]
key = {'a':1,'b':2,'c':4,'d':8,'e':16,'f':32}
door = {'A':1,'B':2,'C':4,'D':8,'E':16,'F':32}
move = [(0,1),(1,0),(0,-1),(-1,0)]

# 시작점 찾기
q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == '0':
            q.append((i,j,0,0)) # x,y,cnt,bit masking
            visit[i][j] = 0
            board[i][j] = '.'
            break
    else:
        continue
    break

while q:
    x,y,cnt,bit = q.popleft()
    for a,b in move:
        dx=x+a; dy=y+b
        if dx>=n or 0>dx or dy>=m or 0>dy or board[dx][dy] == "#":
            continue

        # 이미 왔던 곳인데 열쇠를 더 획득하지 못한 상태
        if not visit[dx][dy] == -1 and visit[dx][dy] | bit == visit[dx][dy]:
            continue
        visit[dx][dy] = bit 

        # 처음 방문
        if visit[dx][dy] == -1:
            visit[dx][dy] = 0

        if board[dx][dy] == '.':
            q.append((dx,dy,cnt+1,bit))
            continue

        if board[dx][dy] == '1':
            print(cnt+1)
            sys.exit()

        k = key.get(board[dx][dy])
        if k != None:
            # 얻은 열쇠 목록을 비트마스킹으로 갱신
            q.append((dx,dy,cnt+1,bit|k))
            continue

        # 열쇠가 있어 문을 열 수 있는 경우 큐에 담음
        d = door.get(board[dx][dy])
        if d | bit == bit:
            q.append((dx,dy,cnt+1,bit))
print(-1)