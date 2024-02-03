# 인간-컴퓨터 상호작용

import sys

input = sys.stdin.readline

name = input().strip()
n = int(input())
arr = [[0 for _ in range(26)] for _ in range(len(name))]
arr[0][ord(name[0]) - 97] = 1
for i in range(1, len(name)):
    arr[i][ord(name[i]) - 97] = 1
    for j in range(26):
        arr[i][j] += arr[i - 1][j]
for i in range(n):
    a = input().split()
    if int(a[1]) > 0:
        res = arr[int(a[2])][ord(a[0]) - 97] - arr[int(a[1]) - 1][ord(a[0]) - 97]
    else:
        res = arr[int(a[2])][ord(a[0]) - 97]
    print(res)
