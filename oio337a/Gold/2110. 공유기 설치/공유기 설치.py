"""
좌표 1개당 집 1개
가장 인접한 두 공유기 사이의 거리를 최대로 하는

1 2 3 4 5 6 7 8 9
0 0   0       0 0
v     v       v
v     v         v

공유기를 설치하는 간격을 최대로 하는 설치 방법

"""
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

s, e, result = 1, house[-1] - house[0], 0

while s <= e:  # s 와 e 가 같아질때까지 반복
    mid = (s + e) // 2
    pre = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= pre + mid:
            count += 1
            pre = house[i]

    if count >= c:
        s = mid + 1
        result = mid
    else:
        e = mid - 1


print(result)
