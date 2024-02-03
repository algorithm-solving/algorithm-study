import sys
input = sys.stdin.readline

# 입력 받기 & 초기값 설정
n = int(input())
su_li = list(map(int, input().split()))
m = int(input())
frefix = [su_li[0]]

# 누적합 구하기
for i in range(1, n):
    frefix.append(frefix[i - 1] + su_li[i])

# 주어진 구간의 누적합 출력
for _ in range(m):
    s, e = map(int, input().split())
    if s == 1:
        print(frefix[e - 1])
    elif s == e:
        print(su_li[s - 1])
    else:
        print(frefix[e - 1] - frefix[s-2])
