import sys
import itertools

li = []
for _ in range(9):
    li.append(int(sys.stdin.readline().rstrip()))

seven = list(itertools.combinations(li, 7))

answer = []
for i in seven:
    if sum(i) == 100:
        answer = sorted(i)
        break

for _ in answer:
    print(_)
