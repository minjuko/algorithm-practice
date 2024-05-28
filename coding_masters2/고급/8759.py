# 사원수

def quater(a, b, c, d, w, x, y, z):
    o = a * w - b * x - c * y - d * z
    p = a * x + b * w + c * z - d * y
    q = a * y - b * z + c * w + d * x
    r = a * z + b * y - c * x + d * w
    return o, p, q, r

a, b, c, d = map(int, input().split())
w, x, y, z = map(int, input().split())
print(*quater(a, b, c, d, w, x, y, z))

