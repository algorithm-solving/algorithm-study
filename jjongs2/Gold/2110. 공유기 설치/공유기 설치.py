from sys import stdin

read = stdin.readline

N, C = map(int, read().split())
positions = sorted(int(read()) for _ in range(N))
first_pos, last_pos = positions[0], positions[-1]
low, high = 1, (last_pos - first_pos) // (C - 1)
while low <= high:
    mid = (low + high) // 2
    indexes = [0]
    for _ in range(C - 1):
        prev_index = indexes[-1]
        curr_pos = positions[prev_index] + mid
        if curr_pos > last_pos:
            high = mid - 1
            break
        for i in range(prev_index + 1, N):
            if positions[i] >= curr_pos:
                indexes.append(i)
                break
    else:
        low = mid + 1
print(high)
