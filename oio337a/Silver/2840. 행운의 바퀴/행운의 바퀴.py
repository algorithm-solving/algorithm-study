
import sys

n, k = map(int, input().split())
li = [0 for _ in range(n)]
idx = 1
for i in range(k):
    a, b = input().split()
    idx -= int(a)
    if li[idx % n] == 0:  # 빈 공간이면 글자 삽입
        li[idx % n] = b
    elif li[idx % n] != b:  # 빈 공간이 아닌데 b 가 아니면 오류
        print('!')
        sys.exit()
for i in li:  # 요소 중복 검사
    if i != 0 and li.count(i) > 1:
        print('!')
        sys.exit()

li.reverse()  # 시계방향으로 출력하려면 리버스 한다.
i = li.index(b)  # 마지막 요소 b 의 인덱스 값 = i
cnt = 0
while cnt < n:
    if li[i] == 0:  # 인덱스의 값이 0 일때 ? 출력
        print('?', end='')
    else:
        print(li[i], end='')
    cnt += 1
    i -= 1
