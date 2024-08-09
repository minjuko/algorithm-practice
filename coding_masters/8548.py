# 팰린드롬 만들기

from itertools import permutations

n = int(input())
words = [input() for _ in range(n)]

permutate = permutations(words)

for case in permutate:
    case = ''.join(case)
    if case == case[::-1]:
        print("YES")
        exit()
print("NO")
