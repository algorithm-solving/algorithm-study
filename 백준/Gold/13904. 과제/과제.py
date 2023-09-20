# 과제

import sys
input = sys.stdin.readline

N = int(input())
quest = [list(map(int, input().split())) for _ in range(N)]
quest.sort(key=lambda x: (-x[1], x[0]))

# max_day = 0
# for i in quest:
#   max_day = max(max_day, i)

max_day = max(quest)[0]

days_list = [0] * (max_day + 1)

for i in quest:
  if days_list[i[0]] == 0:
    days_list[i[0]] = i[1]
  else:
    for j in range(i[0] - 1, 0, -1):
      if days_list[j] == 0:
        days_list[j] = i[1]
        break

print(sum(days_list))
