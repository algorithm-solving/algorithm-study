# 교환
from collections import deque
N, K = map(int, input().split())
M = len(str(N))


def bfs(N, K):
    visited = set()
    visited.add((N, 0))
    q = deque()
    q.append((N, 0))
    answer = 0
    while q:
        n, k = q.popleft()
        if k == K:
            answer = max(answer, n)
            continue
        n = list(str(n))
        for i in range(M-1):
            for j in range(i+1, M):
                if i == 0 and n[j] == '0':
                    continue
                n[i], n[j] = n[j], n[i]
                nn = int(''.join(n))
                if (nn, k+1) not in visited:
                    q.append((nn, k+1))
                    visited.add((nn, k+1))
                n[i], n[j] = n[j], n[i]
    return answer if answer else -1


print(bfs(N, K))