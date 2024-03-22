#유레카 이론
import sys
input = sys.stdin.readline

n = int(input())
tri_num = []
for i in range(1, 45):
    tri_num.append(i*(i+1)//2)

for i in range(n):
    num = int(input())
    for j in tri_num:
        for k in tri_num:
            for l in tri_num:
                if j+k+l == num:
                    print(1)
                    break
            if j+k+l == num:
                break
        if j+k+l == num:
            break
    if j+k+l != num:
        print(0)
