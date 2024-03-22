from sys import stdin

read = stdin.readline


def calc(num):
    if num in counts:
        return counts[num]
    one_third = calc(num // 3) + num % 3
    one_half = calc(num >> 1) + (num & 1)
    count = min(one_third, one_half) + 1
    counts[num] = count
    return count


N = int(read())
counts = {1: 0, 2: 1}
print(calc(N))
