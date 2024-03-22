# 에디터
import sys
input = sys.stdin.readline


## 시간 초과 ##
# string = list(input().rstrip())
# n = int(input())

# cursor = len(string)

# for _ in range(n):
#   command = list(input().split())
#   if command[0] == 'P':
#     string.insert(cursor, command[1])
#     cursor += 1
#   elif command[0] == 'L':
#     if cursor > 0:
#       cursor -= 1
#   elif command[0] == 'D':
#     if cursor < len(string):
#       cursor += 1
#   else:
#     if cursor > 0:
#       string.remove(string[cursor - 1])

# print(''.join(string))


st1 = list(input().rstrip())
st2 = []

for _ in range(int(input())):
  command = list(input().split())
  if command[0] == 'L':
    if st1:
      st2.append(st1.pop())
  elif command[0] == 'D':
    if st2:
      st1.append(st2.pop())
  elif command[0] == 'B':
    if st1:
      st1.pop()
  else:
    st1.append(command[1])

st1.extend(reversed(st2))
print(''.join(st1))