# Knapsack Problem
# 배당 문제

'''
배낭에 담을 수 있는 무게의 최댓값이 정해져 있고,
일정 가치와 무게가 있는 짐들을 배낭에 넣을 때,
가치의 합이 최대가 되도록 짐을 고르는 방법을 찾는 알고리즘

dp table 을 만들고 점진적으로 물건을 선택했을 때 최댓값을 dp에 저장한다.
'''

# 백준 12865 - 평벙한 배낭

n, k = map(int, input().split())
stuffs = [[0, 0]]
knapsack = [[0 for _ in range((k + 1))] for _ in range(n + 1)]

for _ in range(n):
	w, v = map(int, input().split())
	stuffs.append([w, v])

# 냅색 문제 풀이
for i in range(1, n + 1):
	for j in range(1, k + 1):
		weight = stuffs[i][0]
		value = stuffs[i][1]

		if j < weight:
			knapsack[i][j] = knapsack[i - 1][j]
		else:
			knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[n][k])