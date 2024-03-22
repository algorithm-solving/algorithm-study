# 석판 자르기

import sys
input = sys.stdin.readline

# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]

# def check(start_x, end_x, start_y, end_y):
#   jewely_cnt = 0
#   bad_cnt = 0

#   for i in range(start_x, end_x):
#     for j in range(start_y, end_y):
#       if board[i][j] == 2:
#         jewely_cnt += 1
#       elif board[i][j] == 1:
#         bad_cnt += 1
  
#   if jewely_cnt == 0:
#     return 0
#   elif jewely_cnt == 1 and bad_cnt == 0:
#     return 1

# def dfs(start_x, end_x, start_y, end_y, d):
#   flag = check(start_x, end_x, start_y, end_y)
#   if flag == 0 or flag == 1:
#     return flag

#   ans = 0
#   one_cnt = 0
#   if d != 0:
#     for i in range(start_x, end_x):
#       for j in range(start_y, end_y):
#         if board[i][j] == 1:
#           one_cnt += 1
#         if j == end_y - 1 and one_cnt == 1:
#           ans += dfs(start_x, i, start_y, end_y, 0) * dfs(i + 1, end_x, start_y, end_y, 0)
#   else:
#     for i in range(start_y, end_y):
#       for j in range(start_x, end_x):
#         if board[i][j] == 1:
#           one_cnt += 1
#         if j == end_x - 1 and one_cnt == 1:
#           ans += dfs(start_x, end_x, start_y, j, 1) * dfs(start_x, end_x, j + 1, end_y, 1)
#   return ans

# answer = dfs(0, n, 0, n, 0)
# print(answer if answer != 0 else -1)

import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def dfs(start_x, end_x, start_y, end_y, d):
  jewely_cnt = 0
  bad_cnt = 0

  for i in range(start_x, end_x):
    for j in range(start_y, end_y):
      if board[i][j] == 2:
        jewely_cnt += 1
      elif board[i][j] == 1:
        bad_cnt += 1
  
  if jewely_cnt == 0:
    return 0
  elif jewely_cnt == 1 and bad_cnt == 0:
    return 1
  
  ans = 0
  if d != 0:
    for i in range(start_x, end_x):
      flag = 0
      for j in range(start_y, end_y):
        if board[i][j] == 1:
          flag = 1
        if board[i][j] == 2:
          flag = 0
          break
      if flag:
          ans += dfs(start_x, i, start_y, end_y, 0) * dfs(i + 1, end_x, start_y, end_y, 0)
  else:
    for j in range(start_y, end_y):
      flag = 0
      for i in range(start_x, end_x):
        if board[i][j] == 1:
          flag = 1
        if board[i][j] == 2:
          flag = 0
          break
      if flag:
          ans += dfs(start_x, end_x, start_y, j, 1) * dfs(start_x, end_x, j + 1, end_y, 1)
  return ans

answer = dfs(0, n, 0, n, 0)
answer += dfs(0, n, 0, n, 1)
print(answer if answer != 0 else -1)

'''
1. board를 순회하며 2와 1을 찾는다.
  1-1. 보석이 없다면 0을 리턴
  1-2. 보석이 1개이고 불순물이 없다면 1 리턴
2. 행열 을 각각 순회하며 1이 1개인지 찾는다.
  불순물 갯수가 1개라면 해당 행열을 자른뒤 재귀 순회

'''

# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]
# bul_list = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 1]
