from itertools import combinations
from sys import stdin

read = stdin.readline

VOWELS = set('aeiou')

passwords = []
L, _ = map(int, read().split())
letters = sorted(read().split())
for c in combinations(letters, L):
    if 0 < len(set(c) & VOWELS) <= L - 2:
        passwords.append(''.join(c))
print('\n'.join(passwords))
