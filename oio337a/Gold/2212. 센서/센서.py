# 센서

import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

point_list = list(map(int, input().split()))
point_list.sort()

diff_list = [b - a for a, b in zip(point_list[:-1], point_list[1:])]
diff_list.sort()

print(sum(diff_list[:N-K]))