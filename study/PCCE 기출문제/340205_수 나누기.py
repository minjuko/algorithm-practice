number = int(input())

answer = 0

# 두 자리씩 계속 자르기 : 오른쪽 두 자리 더하고 더한 두 자리 제거
while number > 0:
    answer += number % 100
    number //= 100

print(answer)