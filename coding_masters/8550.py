# 예쁜 수

n = input()

def solve(k):
    if k == '':
        return
    if int(n) % int(k) == 0:
        print("YES")
        exit()
    else:
        solve(k[1:])
        solve(k[:-1])

solve(n[1:])
solve(n[:-1])
print("NO")
