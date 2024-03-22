# 박스 채우기

# import sys
# input = sys.stdin.readline

# length, width, height = map(int, input().split())
# n = int(input())
# cubes = [list(map(int, input().split())) for _ in range(n)]

# cubes.sort(key=lambda x: -x[0])

# def fill(length, width, height, cubes):
#     if length == 0 or width == 0 or height == 0:
#         return 0

#     for cube in cubes:
#         if cube[0] > length or cube[0] > width or cube[0] > height:
#             continue

#         if cube[1] > 0:
#             cube[1] -= 1
#             return 1 + fill(length, width, height - cube[0], cubes) + fill(cube[0], width - cube[0], cube[0], cubes) + fill(length - cube[0], width, cube[0], cubes)
#         else:
#             continue

#     return -1

# print(fill(length, width, height, cubes))

# 1. 박스를 채울 수 있는 큐브를 내림차순으로 정렬한다.
# 2. 큐브를 하나씩 꺼내서 박스를 채울 수 있는지 확인한다.
# 3. 박스를 채울 수 있다면 박스를 채우고 1을 리턴한다.
# 4. 박스를 채울 수 없다면 다음 큐브를 확인한다.


import sys
input = sys.stdin.readline


length, width, height = map(int, input().split())
total = length * width * height
N = int(input())
cube = [tuple(map(int, input().split())) for _ in range(N)]
cube.sort(reverse=True)

answer, total_now = 0, 0
for c_idx, c_cnt in cube:
    total_now *= 8 # 다음 순서 = 이전 정육면체 부피의 1/8이므로 이전까지의 개수에 8을 곱해줌 (예 : 4*4*4 1개 = 2*2*2 8개)
    c_len = 2**c_idx
    
    cnt_limit = (length // c_len) * (width // c_len) * (height // c_len) - total_now # 현재 공간에 채울 수 있는 개수 - 지금까지 채운 개수
    cnt_limit = min(c_cnt, cnt_limit) # 실제로 채우기 가능한 개수
    
    answer += cnt_limit
    total_now += cnt_limit

if total_now == total:
    print(answer)
else:
    print(-1)