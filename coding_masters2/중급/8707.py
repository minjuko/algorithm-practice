# Anti Multiply Array

from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

permute = list(permutations(a, 4))
flag = 0

for p in permute:
    if p[0]*p[1] == p[2]*p[3]:
        flag = 1
        break

if flag:
    print("YES")
else:
    print("NO")