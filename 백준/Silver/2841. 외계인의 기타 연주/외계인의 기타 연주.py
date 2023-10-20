from sys import stdin

read = stdin.readline

STRING_COUNT = 6

N, P = map(int, read().split())
move = 0
strings = [[0] for _ in range(STRING_COUNT)]
for _ in range(N):
    n, fret = map(int, read().split())
    string = strings[n - 1]
    while fret < string[-1]:
        string.pop()
        move += 1
    if fret > string[-1]:
        string.append(fret)
        move += 1
print(move)
