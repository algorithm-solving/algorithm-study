#분해합

n = int(input())

for i in range(1, n+1):
    num = list(map(int, str(i)))
    num_sum = i + sum(num)
    if num_sum == n:
        print(i)
        break
    if i == n:
        print(0)
