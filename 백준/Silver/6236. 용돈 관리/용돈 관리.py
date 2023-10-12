from sys import stdin

read = stdin.readline


def min_withdrawal(withdrawal_count, expenses):
    low, high = max(expenses), sum(expenses)
    if withdrawal_count >= high / low:
        return low
    while high - low > 1:
        mid = (low + high) // 2
        count = 1
        left = mid
        for e in expenses:
            left -= e
            if left < 0:
                count += 1
                left = mid - e
        if count > M:
            low = mid
        else:
            high = mid
    return high


N, M = map(int, read().split())
expenses = [int(read()) for _ in range(N)]
print(min_withdrawal(M, expenses))
