# 압축된 수열

n, m = map(int, input().split())
files = list(map(int, input().split()))

arr = {}
def convert(i, file):
    if i == 10 or file < i:
        return str(file)

    tmp = ''
    while file:
        tmp += str(arr[file % i])
        file //= i
    return tmp[::-1]

for i in range(0, 62):
    if i < 10:
        arr[i] = i
    elif i < 36:
        arr[i] = chr(i + ord('A') - 10)
    else:
        arr[i] = chr(i + ord('a') - 36)

for i in range(10, 63):
    tmp2 = ''
    for file in files:
        tmp2 += convert(i, file)
        tmp2 += ' '
    if len(tmp2) <= m+1:
        print(i)
        break
else:
    print(-1)
