# 캠핑
import sys
input = sys.stdin.readline

i = 1
while True:
  L, P, V = map(int, input().split())
  if sum([L, P, V]) == 0:
    break
  
  answer = 0
  answer += (V//P)*L
  answer += min(V%P, L)
  print(f"Case {i}: {answer}")
  i+=1