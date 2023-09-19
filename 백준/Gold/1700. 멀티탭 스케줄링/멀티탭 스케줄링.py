# 멀티탬 스케쥴링

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
if N >= K:
  print(0)
  exit()

stuff_list = list(map(int, input().split()))

plug = set()
cnt = 0

def find_latest(stuff_list, plug):
  latest = -1
  for i in plug:
    if i not in stuff_list:
      return i
    else:
      latest = max(latest, stuff_list.index(i))
  return stuff_list[latest]

for i in range(K):
  if stuff_list[i] in plug:
    continue
  elif len(plug) < N:
    plug.add(stuff_list[i])
  else:
    latest = find_latest(stuff_list[i+1:], plug)
    plug.remove(latest)
    plug.add(stuff_list[i])
    cnt += 1

print(cnt)

