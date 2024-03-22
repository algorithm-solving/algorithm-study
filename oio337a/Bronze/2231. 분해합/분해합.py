
n = int(input())
if n < 55:
  for i in range(1, n+1):
      num = list(map(int, str(i)))
      num_sum = i + sum(num)
      if num_sum == n:
          print(i)
          break
      if i == n:
          print(0)
else:
  for i in range(n-54, n+1):
      num = list(map(int, str(i)))
      num_sum = i + sum(num)
      if num_sum == n:
          print(i)
          break
      if i == n:
          print(0)
