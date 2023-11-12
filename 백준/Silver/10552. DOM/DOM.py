# DOM

import sys
input = sys.stdin.readline

n, m, p = map(int, input().split())

hateDic = {}
visitDic = {}

visit = [0 for _ in range(n)]
board = []
for i in range(n):
  favourite, hated = map(int, input().split())
  hate_P = hateDic.get(hated, -1)
  if hate_P == -1:
    hateDic[hated] = i
  board.append([favourite, hated])

cnt = 0
while True:
  hate_person = hateDic.get(p, -1)

  if hate_person == -1:
    print(cnt)
    break

  if visit[hate_person]:
    print(-1)
    break
  else:
    visit[hate_person] = 1
  p = board[hate_person][0]
  cnt += 1