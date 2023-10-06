# 예산
# https://www.acmicpc.net/problem/2512

import sys

input = sys.stdin.readline

n = int(input())
tax_li = list(map(int, input().split()))
goal_money = int(input())

start = 0
end = max(tax_li)

while start <= end:
    mid = (start + end) // 2
    num = 0
    for i in tax_li:
        if i >= mid:
            num += mid
        else:
            num += i
    if num <= goal_money:
        start = mid + 1
    else:
        end = mid - 1
print(end)
