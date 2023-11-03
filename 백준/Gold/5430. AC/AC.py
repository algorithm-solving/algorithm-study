from sys import stdin

read = stdin.readline

results = []
T = int(read())
for _ in range(T):
    p = read().strip()
    n = int(read())
    raw_nums = read()
    nums = raw_nums.strip('[]\n').split(',') if n > 0 else []
    start, end, step = 0, n, 1
    for func in p:
        if func == 'R':
            step *= -1
            continue
        if step > 0:
            start += 1
        else:
            end -= 1
    results.append(f"[{','.join(nums[start:end][::step])}]" if start <= end else 'error')
print('\n'.join(results))
