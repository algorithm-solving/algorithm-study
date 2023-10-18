from sys import stdin

read = stdin.readline

results = []
T = int(read())
for _ in range(T):
    string = read().strip()
    while '()' in string:
        string = string.replace('()', '')
    results.append('YES' if not string else 'NO')
print('\n'.join(results))
