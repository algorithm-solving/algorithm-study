from itertools import product
from sys import stdin


def find_k_nums(k_str):
    nums = [{int(k_str * length)} for length in range(1, 9)]
    for i in range(1, 8):
        for left in range(i // 2 + 1):
            right = i - 1 - left
            for n1, n2 in product(nums[left], nums[right]):
                lhs, rhs = max(n1, n2), min(n1, n2)
                for k_num in (lhs + rhs, lhs - rhs, lhs * rhs, lhs // rhs):
                    if k_num == 0:
                        continue
                    nums[i].add(k_num)
    return nums


def make_k_dex(nums):
    dex = dict()
    for i in range(8):
        for num in nums[i]:
            if num in dex:
                continue
            dex[num] = str(i + 1)
    return dex


K = stdin.readline().strip()
_ = stdin.readline()
k_nums = find_k_nums(K)
k_dex = make_k_dex(k_nums)
results = []
for a in map(int, stdin.read().splitlines()):
    results.append(k_dex.get(a, 'NO'))
print('\n'.join(results))
