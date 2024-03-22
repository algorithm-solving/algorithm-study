from sys import stdin

read = stdin.readline

INCORRECT_COEFF = 20
PROBLEM_COUNT = 11

time = penalty = 0
predicts = [tuple(map(int, input().split())) for _ in range(PROBLEM_COUNT)]
for D, V in sorted(predicts):
    time += D
    penalty += time + INCORRECT_COEFF * V
print(penalty)
