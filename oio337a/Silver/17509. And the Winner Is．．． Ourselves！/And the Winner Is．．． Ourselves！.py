# And the Winner Is... Ourselves!

import sys
input = sys.stdin.readline

curTime = []
for _ in range(11):
    curTime.append(list(map(int, input().split())))
curTime.sort()

temp = 0
penalty = 0
for i in range(11):
    penalty += temp + curTime[i][0]
    temp += curTime[i][0]
    penalty += 20 * curTime[i][1]
print(penalty)