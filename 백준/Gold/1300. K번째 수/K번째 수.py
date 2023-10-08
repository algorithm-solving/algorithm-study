# k번째 수
# https://www.acmicpc.net/problem/1300

"""
0 1 2 3 4 5
1 1 2 3 4 5
2 2 4 6 8 10
3 3 6 9 12 15
4 4 8 12 16 20
5 5 10 15 20 25
"""
#
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# k = int(input())
#
# b = [i * j for i in range(1, n + 1) for j in range(1, n + 1)]
#
# b.sort()
# print(b[k])

n = int(input())
k = int(input())

def binary_search(target, start, end):
    while (start <= end):
        mid = (start + end) // 2

        cnt = 0
        for i in range(1, n + 1):
            cnt += min(mid//i, n)

        if cnt >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start

print(binary_search(k, 1, n * n))