import sys
input = sys.stdin.readline

"""
1. 입력된 인덱스를 dfs함수에 트리 배열과 함께 전달한다.

2. dfs함수

  2-1. 전달받은 인덱스의 배열 값을 삭제한다는 의미로 -2로 바꾼다. (-1은 루트노드와 겹치므로 피한다.)

  2-2. 배열 전체를 탐색하며, 방금 삭제한 인덱스를 부모노드로 가지는 노드를 찾아 dfs함수를 재귀호출한다.

3. 재귀가 끝나면 삭제될 노드들은 전부 -2로 갱신되어있으므로,

   -2가 아니면서, 다른 노드의 부모노드도 아닌 원소를 찾을 때마다 count를 1씩 늘린다.
"""
def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)


n = int(input())
arr = list(map(int, input().split()))
k = int(input())
count = 0

dfs(k, arr)
count = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        count += 1
print(count)
