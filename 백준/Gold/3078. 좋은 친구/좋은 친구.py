# 좋은 친구


from sys import stdin
from collections import deque
input = stdin.readline

N, K = map(int, input().split())
grade = [0] * 21
student = deque()
count = 0
for _ in range(N):
    a = len(input().rstrip())
    student.append(a)
    grade[a] += 1
    if len(student) > 0:
        if len(student) > K+1:
            old = student.popleft()
            grade[old]-=1
        count += (grade[a]-1)
print(count)
