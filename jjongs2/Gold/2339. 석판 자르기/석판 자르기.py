from sys import stdin

read = stdin.readline


def divide(r_begin, c_begin, r_end, c_end, direction):
    positions = {'1': [], '2': []}
    for r in range(r_begin, r_end):
        for c in range(c_begin, c_end):
            state = slate[r][c]
            if state == '0':
                continue
            positions[state].append((r, c))
    impurities, crystals = positions['1'], positions['2']
    if len(impurities) != len(crystals) - 1:
        return 0
    if not impurities:
        return 1
    count = 0
    crystal_rows, crystal_cols = map(set, zip(*crystals))
    for r, c in impurities:
        if direction != '-' and r not in crystal_rows | {r_begin, r_end - 1}:
            top = divide(r_begin, c_begin, r, c_end, '-')
            bottom = divide(r + 1, c_begin, r_end, c_end, '-')
            count += top * bottom
        if direction != '|' and c not in crystal_cols | {c_begin, c_end - 1}:
            left = divide(r_begin, c_begin, r_end, c, '|')
            right = divide(r_begin, c + 1, r_end, c_end, '|')
            count += left * right
    return count


N = int(read())
slate = tuple(read().split() for _ in range(N))
count = divide(0, 0, N, N, '+')
print(count if count > 0 else -1)
