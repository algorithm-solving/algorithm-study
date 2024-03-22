
import sys
input = sys.stdin.readline

# 1. 재귀 풀이 방식
N, r, c = map(int, input().split())

def sol(N, r, c):

	if N == 0:
		return 0
        
	return 2*(r%2)+(c%2) + 4*sol(N-1, int(r/2), int(c/2))

print(sol(N, r, c))