# 팰린드롬 만들기
# 역순으로 읽어도 같은 낱말
# 문자열들을 재배열하여 하나의 팰린드롬 문자열을 만들 수 있는지 판단

from collections import Counter
n = int(input())
words = [input() for _ in range(n)]

cnt = Counter(''.join(words))
odd = sum(1 for cnt in cnt.values() if cnt % 2)

if odd > 1:
    print("NO")
else:
    print("YES")