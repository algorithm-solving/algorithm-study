from sys import stdin

read = stdin.readline


def assign_budget(requests, total_budget):
    low, high = 1, max(requests)
    if sum(requests) <= total_budget:
        return high
    while high - low > 1:
        mid = (low + high) // 2
        budget = sum(min(r, mid) for r in requests)
        if budget > total_budget:
            high = mid
        else:
            low = mid
    return low


N = int(read())
requests = tuple(map(int, read().split()))
M = int(read())
print(assign_budget(requests, M))
