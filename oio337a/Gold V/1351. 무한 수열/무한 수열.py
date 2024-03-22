# 무한수열

import sys
input = sys.stdin.readline

def calculate_A(N, P, Q, memo):
    if N == 0:
        return 1
    if N in memo:
        return memo[N]
    else:
        memo[N] = calculate_A(N // P, P, Q, memo) + calculate_A(N // Q, P, Q, memo)
        return memo[N]

def find_AN(N, P, Q):
    memo = {}
    return calculate_A(N, P, Q, memo)

# 예시 사용
N, P, Q = map(int, input().split())
memo = {}
print(calculate_A(N, P, Q, memo))