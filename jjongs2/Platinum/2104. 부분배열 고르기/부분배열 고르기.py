from sys import stdin

read = stdin.readline

MIN_VALUE = 0

N = int(read())
nums = tuple(map(int, read().split())) + (MIN_VALUE,)
max_score = 0
stack = [(MIN_VALUE, None)]
for num in nums:
    range_sum = 0
    while num < stack[-1][0]:
        popped_num, popped_range_sum = stack.pop()
        range_sum += popped_range_sum + popped_num
        max_score = max(range_sum * popped_num, max_score)
    stack.append((num, range_sum))
print(max_score)
