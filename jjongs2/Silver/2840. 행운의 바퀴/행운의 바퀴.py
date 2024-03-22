from sys import stdin

read = stdin.readline


def determine_wheel(letter_count, spins):
    wheel = ['?' for _ in range(letter_count)]
    index = 0
    while spins:
        move_count, letter = spins.pop()
        if wheel[index] == '?':
            if letter in wheel:
                return '!'
            wheel[index] = letter
        elif wheel[index] != letter:
            return '!'
        index = (index + int(move_count)) % letter_count
    return ''.join(wheel)


N, K = map(int, read().split())
spins = [read().split() for _ in range(K)]
print(determine_wheel(N, spins))
