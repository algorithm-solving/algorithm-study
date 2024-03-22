# Breed Counting

import sys
input = sys.stdin.readline

n, q = map(int, input().split())
cows = [int(input()) for _ in range(n)]

# 누적합 전처리
prefix = [(0,0,0)]
for i in range(n):
  one, two, three = prefix[-1]
  if cows[i] == 1:
    one += 1
  elif cows[i] == 2:
    two += 1
  else:
    three += 1
  prefix.append((one, two, three))

# 구간합 출력
for i in range(q):
  s, e = map(int, input().split())
  if s == 1:
    print(*prefix[e])
  else:
    e_1, e_2, e_3 = prefix[e]
    s_1, s_2, s_3 = prefix[s - 1]
    print(e_1 - s_1, e_2 - s_2, e_3 - s_3)