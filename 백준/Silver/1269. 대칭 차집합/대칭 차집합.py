from sys import stdin

read = stdin.readline

_ = read()
A = set(read().split())
B = set(read().split())
print(len(A - B) + len(B - A))
