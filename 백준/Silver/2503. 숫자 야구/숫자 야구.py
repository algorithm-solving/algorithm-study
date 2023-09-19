from itertools import permutations
from sys import stdin

read = stdin.readline


def ball_count(answer, case):
    strike = ball = 0
    for index, digit in enumerate(case):
        if digit not in answer:
            continue
        if digit == answer[index]:
            strike += 1
        else:
            ball += 1
    return strike, ball


cases = list(permutations(range(1, 10), 3))
N = int(read())
for _ in range(N):
    num, strike, ball = read().split()
    input_case = tuple(map(int, num))
    count = (int(strike), int(ball))
    cases = [c for c in cases if ball_count(c, input_case) == count]
print(len(cases))
