# ∑|ΔEasyMAX|

import sys
input = sys.stdin.readline

n, q = map(int, input().split())
bpm = list(map(int, input().split()))

# 누적합 전처리
prefix = [0]
for i in range(n - 1):
  prefix.append(abs(bpm[i + 1] - bpm[i]) + prefix[-1])

# 구간합 출력
for i in range(q):
  s, e = map(int, input().split())
  print(prefix[e - 1] - prefix[s - 1])
