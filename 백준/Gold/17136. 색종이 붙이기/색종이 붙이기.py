from sys import stdin

GRID_SIZE = 10
TYPE_COUNT = 5
MASKS = [((1 << i) - 1) << GRID_SIZE - i for i in range(TYPE_COUNT + 1)]


def find_sizes(r0, c0):
    sizes = []
    for size in range(TYPE_COUNT, 0, -1):
        if subgrids[size] == 0:
            continue
        if r0 + size > GRID_SIZE or c0 + size > GRID_SIZE:
            continue
        mask = MASKS[size] >> c0
        for r in range(r0, r0 + size):
            if grid[r] & mask != mask:
                break
        else:
            sizes.append(size)
    return sizes


def mask_off(r0, c0, size):
    mask = MASKS[size] >> c0
    for r in range(r0, r0 + size):
        grid[r] ^= mask


def mask_on(r0, c0, size):
    mask = MASKS[size] >> c0
    for r in range(r0, r0 + size):
        grid[r] |= mask


def search(count):
    if count >= subgrids[0]:
        return
    for r in range(GRID_SIZE):
        if grid[r] == 0:
            continue
        for c in range(GRID_SIZE):
            if grid[r] & MASKS[1] >> c == 0:
                continue
            for size in find_sizes(r, c):
                mask_off(r, c, size)
                subgrids[size] -= 1
                search(count + 1)
                mask_on(r, c, size)
                subgrids[size] += 1
            return
    subgrids[0] = min(subgrids[0], count)


grid = [int(''.join(line.split()), 2) for line in stdin.read().splitlines()]
subgrids = [25, 5, 5, 5, 5, 5]
search(0)
min_count = subgrids[0]
print(min_count if min_count < 25 else -1)
