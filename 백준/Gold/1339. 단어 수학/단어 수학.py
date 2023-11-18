from sys import stdin

N = int(stdin.readline())
words = stdin.read().splitlines()
coeffs = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
for word in words:
    max_i = len(word) - 1
    for i, char in enumerate(word):
        coeffs[char] += pow(10, max_i - i)
max_sum = 0
for i, coeff in enumerate(sorted(coeffs.values(), reverse=True)):
    if coeff == 0:
        break
    max_sum += coeff * (9 - i)
print(max_sum)
