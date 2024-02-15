# 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dogam = dict()
index_dogam = dict()
for i in range(1, n + 1):
  pokemon = input().rstrip()
  dogam[i] = pokemon
  index_dogam[pokemon] = i 

for _ in range(m):
  temp = input().rstrip()
  try:
    a = int(temp)
    print(dogam[a])
  except:
    print(index_dogam[temp])