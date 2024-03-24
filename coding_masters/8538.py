# 별찍기

n = int(input())
answer = []

def solve(n):
    if n==1:
        return ['*']
    if n<=0:
        return []
    tmp = solve(n-1)
    row = []

    row += [i+' '*len(i) + i for i in tmp]
    row += [' '*len(i) + i + ' '*len(i) for i in tmp]
    row += [i + ' '*len(i) + i for i in tmp]

    return row

answer = '\n'.join(solve(n))
print(answer)

