import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    li = input().strip()
    left, right = [], []
    for i in li:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    left.extend(reversed(right))
    print(''.join(left))
