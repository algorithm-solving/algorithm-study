# Generic Queries

import sys
input = sys.stdin.readline

n, q = map(int, input().split())

# 수열 입력
arr = list(map(int, input().split()))

# prefix sum 배열 전처리
xor_arr = [0]
for i in arr:
  xor_arr.append(xor_arr[-1] ^ i)

# 쿼리 별 처리
total_xor = 0
for _ in range(q):
  i, j = map(int, input().split())
  temp = xor_arr[j] ^ xor_arr[i - 1]
  total_xor = total_xor ^ temp

# 결과 출력
print(total_xor)
