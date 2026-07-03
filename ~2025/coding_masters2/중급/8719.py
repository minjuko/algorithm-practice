# 신소재 개발

arr = list(map(int, input().split()))
arr.sort(reverse=True)
a, b, c = arr[0], arr[1], arr[2]
total = sum(arr)

if a > (total + 1) / 2:
    print("NO")
else:
    min_x = total // 2
    max_x = (total // 3) * 2 + (total % 3 > 0)
    cur_x = total - a

    if cur_x == min_x:
        print("YES")
    else:
        if total % 3 == 2:
            tmp = max_x - cur_x - 1
            print("YES" if b - c <= tmp * 3 + 1 else "NO")
        else:
            print("YES" if b - c <= (max_x - cur_x) * 3 else "NO")
