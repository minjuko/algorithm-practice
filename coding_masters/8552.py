# 밑장 빼기

n = int(input())
nums = list(map(int, input().split()))

start, end = 0, n-1
answer = 1

while start <= end:
    if nums[start] == answer:
        start += 1
    elif nums[end] == answer:
        end -= 1
    else:
        break

    if answer == n:
        print("YES")
        exit()
    answer += 1
print("NO")