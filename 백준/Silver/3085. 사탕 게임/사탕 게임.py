from sys import stdin

read = stdin.readline


def max_consecution(line, size):
    max_count = count = 1
    for i in range(1, size):
        count = count + 1 if line[i] == line[i - 1] else 1
        max_count = max(count, max_count)
    return max_count


def find_local_max(board, size):
    local_max = 1
    for r in range(size):
        row = board[r]
        row_max = max_consecution(row, size)
        local_max = max(row_max, local_max)
        for c in range(size - 1):
            row[c], row[c + 1] = row[c + 1], row[c]
            row_max = max_consecution(row, size)
            col1 = [board[i][c] for i in range(size)]
            col1_max = max_consecution(col1, size)
            col2 = [board[i][c + 1] for i in range(size)]
            col2_max = max_consecution(col2, size)
            local_max = max(row_max, col1_max, col2_max, local_max)
            row[c], row[c + 1] = row[c + 1], row[c]
    return local_max


N = int(read())
board = [list(read().strip()) for _ in range(N)]
board_max = find_local_max(board, N)
transposed = list(map(list, zip(*board)))
transposed_max = find_local_max(transposed, N)
print(max(board_max, transposed_max))
