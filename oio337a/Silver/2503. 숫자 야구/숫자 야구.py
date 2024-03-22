# 숫자 야구
import sys
input = sys.stdin.readline

n = int(input())
num = []
answer = 0
for i in range(n):
    num.append(list(map(int, input().split())))
for i in range(123, 988):
    i = str(i)
    if i[0] == i[1] or i[1] == i[2] or i[0] == i[2] or i[0] == '0' or i[1] == '0' or i[2] == '0':
        continue
    for j in range(n):
        strike = 0
        ball = 0
        for k in range(3):
            if i[k] == str(num[j][0])[k]:
                strike += 1
            elif i[k] in str(num[j][0]):
                ball += 1
        if strike != num[j][1] or ball != num[j][2]:
            break
    else:
        answer += 1
print(answer)