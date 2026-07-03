# 분수를 소수로

# 정확한 소수 표현
from decimal import Decimal, getcontext

p, q = map(int, input().split()) # 분자, 분모
n = int(input()) # 소수점 자릿수

getcontext().prec = n
tmp = Decimal(p) / Decimal(q)
print(round(tmp, n))
