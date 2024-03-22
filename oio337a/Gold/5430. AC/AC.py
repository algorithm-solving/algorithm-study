import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    f = list(input().rstrip())
    li_len = int(input())
    li = deque(input().rstrip()[1:-1].split(","))

    rev_flag = 0
    flag = 0
    if li_len == 0:
        li = []
    for i in f:
        if i == 'R':
            rev_flag += 1
        elif i == 'D':
            if len(li) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev_flag % 2 == 0:
                    li.popleft()
                else:
                    li.pop()
    if flag == 0:
        if rev_flag % 2 == 0:
            print("[" + ",".join(li) + "]")
        else:
            li.reverse()
            print("[" + ",".join(li) + "]")
