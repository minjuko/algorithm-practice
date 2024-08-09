# 방향 추적

n = int(input())

for i in range(0, n):
    a, b = map(int, input().split(" "))

    if i == 0:
        tmp = [a, b]
    else:
        if a < tmp[0]:
            if b < tmp[1]:
                if abs(tmp[0] - a) != 0:
                    print(1, abs(tmp[0] - a))
                else:
                    print(4, abs(tmp[1] - b))
            else:
                if abs(tmp[0] - a) != 0:
                    print(3, abs(tmp[0] - a))
                else:
                    print(4, abs(tmp[1] - b))
        else:
            if b < tmp[1]:
                if abs(tmp[0] - a) != 0:
                    print(1, abs(tmp[0] - a))
                else:
                    print(4, abs(tmp[1] - b))
            else:
                if abs(tmp[0] - a) != 0:
                    print(1, abs(tmp[0] - a))
                else:
                    print(2, abs(tmp[1] - b))
        tmp = [a, b]
