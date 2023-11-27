# 좋은 수열

import sys
input = sys.stdin.readline

def check(num: str):
    l = len(num)
    for idx in range(1, l//2 + 1):
        if num[-idx:] == num[-(idx*2):-idx]:
            return False
    return True

def recursive(num: str):
    if len(num) == n:
        print(num)
        exit()
    for i in '123':
        if check(num + str(i)):
            recursive(num + str(i))
    return

n = int(input())
recursive('1')