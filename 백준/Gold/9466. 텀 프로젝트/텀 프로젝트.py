from sys import stdin

read = stdin.readline

results = []
T = int(read())
for _ in range(T):
    n = int(read())
    selections = [0] + list(map(int, read().split()))
    count = n
    visited = [False for _ in range(n + 1)]
    for student in range(1, n + 1):
        if visited[student]:
            continue
        team = []
        while not visited[student]:
            visited[student] = True
            team.append(student)
            student = selections[student]
        if student in team:
            count -= len(team) - team.index(student)
    results.append(count)
print('\n'.join(map(str, results)))
