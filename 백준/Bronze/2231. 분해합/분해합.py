from sys import stdin

read = stdin.readline


def digit_sum(n):
    return n + sum(int(digit) for digit in str(n))


N = int(read())
length = len(str(N))
min_M = max(0, N - 9 * length) + 1
generator = (n for n in range(min_M, N) if digit_sum(n) == N)
result = next(generator, 0)
print(result)
