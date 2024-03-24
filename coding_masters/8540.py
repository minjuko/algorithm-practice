# 순환소수

p, q = map(int, input().split())
a = []
b = []
tmp = p*10
prefix = '0.'

while True:
    if tmp == 0:
        break
    if a and tmp in a:
        idx = a.index(tmp)
        print(prefix+''.join(b[:idx])+'{'+''.join(b[idx:])+'}')
        exit()

    c, d = tmp//q, tmp%q
    a.append(tmp)
    b.append(str(c))
    tmp = d*10

print(prefix+''.join(b))