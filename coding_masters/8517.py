# 피보나치 피보나치 수열
# 피보나치 수열의 각 항을 그 수만큼 반복해서 만든 수열

# 피보나치 피보나치 수열의 a항부터 b항까지의 합 출력

# 피보나치 함수 정의
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 2) + fibo(n - 1)

# 입력 받기
a, b = map(int, input().split())

# 피보나치 피보나치 수열 생성
fibofibo = []
index = 0
num = 1

# 피보나치 피보나치 수열 만들기
while True:
    temp = fibo(num)

    for i in range(temp):
        fibofibo.append(temp)
        index += 1

        if index == 100:
            break

    if index == 100:
        break

    num += 1

# 합 계산
sum = 0
for i in range(a, b + 1):
    sum += fibofibo[i - 1]

print(sum)
