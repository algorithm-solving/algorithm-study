from itertools import product
from sys import stdin

BLANK = 0
L = 9


def b(r, c):
    return r // 3 * 3 + c // 3


def is_valid(r, c, mask):
    if rows[r] & mask != 0:
        return False
    if cols[c] & mask != 0:
        return False
    if boxes[b(r, c)] & mask != 0:
        return False
    return True


def mask_off(r, c, mask):
    rows[r] &= ~mask
    cols[c] &= ~mask
    boxes[b(r, c)] &= ~mask


def mask_on(r, c, mask):
    rows[r] |= mask
    cols[c] |= mask
    boxes[b(r, c)] |= mask


def fill_blanks(index, count):
    if index == count:
        return True
    r, c = blanks[index]
    for num in range(1, L + 1):
        mask = 1 << num
        if not is_valid(r, c, mask):
            continue
        board[r][c] = num
        mask_on(r, c, mask)
        if fill_blanks(index + 1, count):
            return True
        board[r][c] = BLANK
        mask_off(r, c, mask)
    return False


board = [list(map(int, line.split())) for line in stdin.read().splitlines()]
rows = [0 for _ in range(L)]
cols, boxes = rows.copy(), rows.copy()
blanks = []
for r, c in product(range(L), repeat=2):
    num = board[r][c]
    if num == BLANK:
        blanks.append((r, c))
        continue
    mask_on(r, c, 1 << num)
fill_blanks(0, len(blanks))
print('\n'.join(' '.join(map(str, row)) for row in board))
