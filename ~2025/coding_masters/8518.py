# 직각 삼각형

# 직각 삼각형 판별

a, b, c = map(int, input().split())

if a ** 2 + b ** 2 == c ** 2:
    print("YES")
else:
    print("NO")