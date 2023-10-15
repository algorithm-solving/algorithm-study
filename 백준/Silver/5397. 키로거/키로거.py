from sys import stdin

read = stdin.readline

case_count = int(read())
results = []
for _ in range(case_count):
    left, right = [], []
    for char in read().strip():
        try:
            if char == '-':
                left.pop()
            elif char == '<':
                right.append(left.pop())
            elif char == '>':
                left.append(right.pop())
            else:
                left.append(char)
        except IndexError:
            pass
    left.extend(reversed(right))
    results.append(''.join(left))
print('\n'.join(results))
