from math import ceil
from sys import stdin

read = stdin.readline

N, atk = map(int, read().split())
max_hp = 0
damage_taken = 0
for _ in range(N):
    t, a, h = map(int, read().split())
    if t == 1:
        damage_taken += a * (ceil(h / atk) - 1)
        max_hp = max(max_hp, damage_taken)
    else:
        atk += a
        damage_taken = max(0, damage_taken - h)
print(max_hp + 1)
