# 팔찌

a = input()
b = input()

for i in range(len(a)):
    if  a == b[i:] + b[:i]:
        print("YES")
        exit()

print("NO")