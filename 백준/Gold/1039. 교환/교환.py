from sys import stdin

N, K = map(int, stdin.read().split())
L = len(str(N))
curr_nums = {N}
while K > 0:
    next_nums = set()
    for n in curr_nums:
        d0 = list(str(n))
        for i in range(L - 1):
            for j in range(i + 1, L):
                if i == 0 and d0[j] == '0':
                    continue
                d = d0[:]
                d[i], d[j] = d[j], d[i]
                next_nums.add(int(''.join(d)))
    curr_nums = next_nums
    K -= 1
print(max(curr_nums) if curr_nums else -1)
