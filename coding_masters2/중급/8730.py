# 주사위 굴리기

def solve(nums, ch):
    next = nums[:]

    if ch == 1:
        next[0], next[2], next[4], next[5] = nums[4], nums[5], nums[2], nums[0]
    elif ch == 2:
        next[1], next[3], next[4], next[5] = nums[4], nums[5], nums[3], nums[1]
    elif ch == 3:
        next[0], next[2], next[4], next[5] = nums[5], nums[4], nums[0], nums[2]
    elif ch == 4:
        next[1], next[3], next[4], next[5] = nums[5], nums[4], nums[1], nums[3]
    return next

w, h = map(int, input().split())
x, y = map(int, input().split())
nums = list(map(int, input().split()))
n = int(input())
chs = list(map(int, input().split()))

result = [[0]*w for _ in range(h)]
result[y][x] = nums[5]

for ch in chs:
    nums = solve(nums, ch)
    if ch == 1 and x+1 < len(result[0]):
        x += 1
    elif ch == 2 and y+1 < len(result):
        y += 1
    elif ch ==3 and x-1 >= 0:
        x -= 1
    elif ch == 4 and y-1 >= 0:
        y -= 1
    result[y][x] = nums[5]

for i in result:
    print(*i)
