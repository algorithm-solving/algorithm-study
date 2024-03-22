def solve(s, e):
    if s == e:
        return A[s] * A[s]
    mid = (s+e)//2
    ret = max(solve(s, mid), solve(mid+1, e))

    left = mid
    right = mid + 1
    _sum = A[left] + A[right]
    min_val = min(A[left], A[right])
    ret = max(ret, min_val * _sum)
    while left > s or right < e:
        if right < e and (left == s or A[left-1] < A[right + 1]):
            right += 1
            _sum += A[right]
            min_val = min(min_val, A[right])
        else:
            left -= 1
            _sum += A[left]
            min_val = min(min_val, A[left])
        ret = max(ret, min_val * _sum)
    return ret

n = int(input())
A = list(map(int, input().split()))
print(solve(0, n-1))