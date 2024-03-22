from sys import stdin


def find_seq(s0):
    if (length := len(s0)) == N:
        return s0
    length += 1
    for char in '123':
        s = s0 + char
        for di in range(1, length // 2 + 1):
            i = length - di
            if s[i:] == s[i - di:i]:
                break
        else:
            if ret := find_seq(s):
                return ret
    return ''


N = int(stdin.read())
print(find_seq('1'))
