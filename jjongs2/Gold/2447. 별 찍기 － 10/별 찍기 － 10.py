from sys import stdin

read = stdin.readline


def draw_fractal(size):
    if size == 1:
        return ['*']
    size //= 3
    fractal = draw_fractal(size)
    top_bottom = [f * 3 for f in fractal]
    middle = [f + ' ' * size + f for f in fractal]
    return top_bottom + middle + top_bottom


N = int(read())
result = draw_fractal(N)
print('\n'.join(result))
