# 풍선 터뜨리기

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))

balloons = []

while q:
  idx, paper = q.popleft()
  balloons.append(idx + 1)

  if paper > 0:
    q.rotate(-(paper - 1))
  else:
    q.rotate(-paper)

print(' '.join(map(str, balloons)))