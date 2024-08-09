# 자연수의 신

n, k = map(int, input().split())
idx = (n+1) // 2

if k <= idx:
    print(2*k-1)
else:
    print(2*(k-idx))