# 떨어진 숫자

a = input() # 떨어뜨린 수
b = input() # 주워담은 수

if sorted(a) == sorted(b):
    print("YES")
else:
    print("NO")