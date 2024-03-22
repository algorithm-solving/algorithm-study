from sys import stdin

read = stdin.readline

A, B, C = map(int, read().split())
print(pow(A, B, C))
