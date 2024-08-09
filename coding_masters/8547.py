# 구조 요원

n = int(input())
x, y = map(int, input().split())


if x == 0:
    print(0)
    exit()
if x>0:
    t_x = x
else:
    t_x = -x
time = [0]*t_x

for i in range(1, t_x+1):
    time[i-1] = ((i**2 + n**2) ** 0.5) / 10 + (((t_x-i)**2 + y**2) ** 0.5) / 5
tmp = time.index(min(time)) + 1

if x>0:
    print(tmp)
else:
    print(-tmp)

