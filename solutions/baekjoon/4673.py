# 셀프 넘버
# d(n) = n + n의 각 자리수
# n은 d(n)의 생성자
# 셀프넘버는 생성자가 없는 숫자
# 1~10000까지의 셀프 넘버 출력

def d(n):
    n = n + sum(map(int, str(n)))
    return n

no_self = set()

for i in range(1, 10001):
    no_self.add(d(i))
    if i not in no_self:
        print(i)
