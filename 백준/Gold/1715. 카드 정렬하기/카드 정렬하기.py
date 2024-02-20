from heapq import heappop
from heapq import heappush
from heapq import heappushpop
from sys import stdin

_ = stdin.readline()
deck_sizes = []
for deck_size in map(int, stdin.read().splitlines()):
    heappush(deck_sizes, deck_size)
count = 0
while len(deck_sizes) > 1:
    combined_deck_size = heappop(deck_sizes) + deck_sizes[0]
    count += combined_deck_size
    heappushpop(deck_sizes, combined_deck_size)
print(count)
