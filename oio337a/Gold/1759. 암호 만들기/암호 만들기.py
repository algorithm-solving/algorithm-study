# 암호 만들기
# https://www.acmicpc.net/problem/1759

import sys
from itertools import combinations
input = sys.stdin.readline

l, c = map(int, input().split())
alpha = sorted(input().split())
mo = ['a', 'e', 'i', 'o', 'u']
result = []

for c in list(combinations(alpha, l)):
    mo_cnt = 0
    ja_cnt = 0
    for char in c:
        if char in mo:
            mo_cnt += 1
        else:
            ja_cnt += 1
    if mo_cnt > 0 and ja_cnt > 1:
        result.append("".join(c))

for i in result:
    print(i)