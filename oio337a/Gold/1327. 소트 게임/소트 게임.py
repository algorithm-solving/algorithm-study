"""
k 보다 오른쪽의 요소의 객수가 많아야 한다. 
오름차순으로 만들 수 없으면 -1 출력
"""

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(input().split())

visited_s = set(''.join(li))
q = deque([[''.join(li), 0]])  # 3 2 1 => ['321', 0]

answer = -1
while(q):
    word, cnt = q.popleft()
    temp_li = list(word)  # [3, 2, 1]

    if temp_li == sorted(temp_li):
        answer = cnt
        break

    is_first = False
    for i in range(n-k+1):
        new_li = list(temp_li)
        target_li = new_li[i:i+k]  # 뒤집어야할 리스트 구간
        target_li.reverse()
        for j in range(k):  # 뒤 집힌 리스트 업데이트
            new_li[i+j] = target_li[j]
        new_word = ''.join(new_li)
        if new_word not in visited_s:
            visited_s.add(new_word)
            q.append([new_word, cnt+1])

print(answer)
