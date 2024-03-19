# 가우스와 정다각형
import sys
input = sys.stdin.readline
# 입력 받기
k = int(input().strip())

# 페르마 소수 리스트
fermat = [3, 5, 17, 257, 65537]
flag = [0] * 5

# k를 페르마 소수로 나누기
for i in range(5):
    while k % fermat[i] == 0 and flag[i] == 0:
        flag[i] += 1
        k //= fermat[i]

# k가 1이면 가우스 다각형
if k == 1:
    print('YES')
else:
    # 2의 거듭제곱 확인
    nums = [4 << i for i in range(55)]
    if k in nums:
        print('YES')
    else:
        print('NO')
