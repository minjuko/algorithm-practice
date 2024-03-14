a, b = map(int, input().split())

def comb(n, r):
    if r == 0 or n == r:
        return 1
    return comb(n-1, r-1) + comb(n-1, r)

# a나 b가 1일 경우 처리
if a == 1 or b == 1:
    print(1)
else:
    print(comb(a, b))
