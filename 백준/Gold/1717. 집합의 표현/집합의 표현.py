import sys
sys.setrecursionlimit(10 ** 5)


def solve():
    n, m = map(int, sys.stdin.readline().split())
    p = [-1] * (n + 1)  # 자기자신의 Root를 기록한 Array

    def find(n):  # 두 원소가 같은 root를 갖는지(같은 집합인지) 확인해주는 함수
        if p[n] < 0:
            return n  # p[root]는 음수
        # 재귀반복을 줄여주는 line, 직선상에서 같은 root를 갖고 있다면 root를 새로 갱신해줌
        p[n] = find(p[n])
        return p[n]

    def union(x, y):  # 두 집합을 합치는 func => 두 가지 root중 임의의 root로 묶기
        a = find(x)  # root search 1
        b = find(y)  # root search 2
        if a == b:
            return  # 이미 a,b의 root가 동일하면 새로 작업해줄 필요 X
        if p[a] > p[b]:  # 더 큰 Rank가 부모노드가 되게끔 하는 작업
            p[b] += p[a]
            p[a] = b
        else:
            p[a] += p[b]
            p[b] = a

    for _ in range(m):
        c, x, y = map(int, sys.stdin.readline().split())
        if c == 0:  # union
            union(x, y)
        else:
            if x == y:
                sys.stdout.write("YES\n")
                continue
            sys.stdout.write("YES\n") if find(
                x) == find(y) else sys.stdout.write("NO\n")


solve()
