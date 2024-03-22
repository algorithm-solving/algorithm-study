import sys
input = sys.stdin.readline

"""
잘려진 나무를 가져간다.
최대한 적게 자른다. 다른말로 최대한 높이 자른 것을 가져간다.

"""
n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    cut_tree = 0
    for i in tree:
        if i >= mid:
            cut_tree += i - mid
    if cut_tree >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
