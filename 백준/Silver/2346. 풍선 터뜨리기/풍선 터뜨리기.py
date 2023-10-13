from sys import stdin

read = stdin.readline

N = int(read())
moves = tuple(map(int, read().split()))
ballons = list(enumerate(moves, start=1))
popped = []
tgt_index = 0
for i in range(N):
    tgt_index %= N - i
    index, move = ballons.pop(tgt_index)
    popped.append(index)
    tgt_index += move - 1 if move > 0 else move
print(*popped)
