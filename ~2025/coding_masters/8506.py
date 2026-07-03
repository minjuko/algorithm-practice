# 구름 별

n = int(input())

for i in range(n):
    if i>=1:
        for j in range(i):
            print(" ", end="")
    print("**", end="")
    print()