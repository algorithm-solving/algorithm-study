# 창고 다각형

import sys
input = sys.stdin.readline

# 기둥 개수
N = int(input())
# 가장 높은 길이와 인덱스, 가장 끝에 있는 번호와 그 때의 높이를 구해준다.
pillar = []
highest = 0
longest = 0
highest_idx = 0
longest_height =0
for i in range(N):
    a,b = map(int, input().split())
    # 왼쪽 면과 높이를 각각 리스트에 넣어준다.
    pillar.append((a,b))
    if b > highest:
        # 가장 높을 때의 인덱스
        highest = b
        highest_idx = a
    if a > longest:
        # 가장 끝에 있는 기둥 번호와 높이
        longest = a
        longest_height = b
#print(highest_idx, highest, longest_height, longest)
# 가장 높은 곳을 기준으로 좌측, 우측으로 나눠서 해준다.
sum = 0
# 높이 기록해줄 배열
arr=[0]*(longest+1)
nopi = 0
# 각 번호에 맞는 높이 기록
for i in range(len(pillar)):
    arr[pillar[i][0]] = pillar[i][1]

# 가장 높은 곳 기준 좌측
for j in range(1,highest_idx):
    # 다음 높이가 이전 높이보다 낮아면, 이전 높이로 통일
    if not arr[j] > arr[j-1]:
        arr[j] = arr[j-1]
# 우측
for k in range(longest, highest_idx, -1):
    # 왼쪽 높이가 오른쪽보다 낮아면 오른쪽높이로 통일
    if not arr[k-1] > arr[k]:
        arr[k-1] = arr[k]

for l in arr:
    sum += l

print(sum)
    
    
