import sys

meter = int(input())
n = int(input())

num1 = []
num2 = []
start = []
end = []

# 출발한 로그와 시간 입력
for _ in range(n):  # 변수 i 사용하지 않으므로 _ 로 변경
    car, s = input().split()
    num1.append(car)
    start.append(s)

# 도착한 로그와 시간 입력
for _ in range(n):  # 변수 i 사용하지 않으므로 _ 로 변경
    car, e = input().split()
    num2.append(car)
    end.append(e)

startTime = []
endTime = []

# 출발, 도착 시간 초로 변환
for i in range(n):
    startH, startM, startS = map(int, start[i].split(':'))
    endH, endM, endS = map(int, end[i].split(':'))

    startTime.append(startH * 3600 + startM * 60 + startS)
    endTime.append(endH * 3600 + endM * 60 + endS)

passTime = [0] * n

# 구간을 통과하는데 걸린 시간
for i in range(n):
    for j in range(n):
        if num1[i] == num2[j]:
            passTime[i] = endTime[j] - startTime[i]

result = []

# 속력 구하기
for i in range(n):
    if passTime[i] == 0:  # 출발점에서 도착점으로 이동하지 않은 경우
        speed = 0
    else:
        speed = (meter / passTime[i]) * 3600
    result.append(str(int(round(speed))))

# 버블 정렬을 사용하여 리스트를 오름차순으로 정렬
for i in range(n - 1):
    for j in range(n - 1 - i):
        if num1[j] > num1[j + 1]:
            num1[j], num1[j + 1] = num1[j + 1], num1[j]
            result[j], result[j + 1] = result[j + 1], result[j]

# 정렬된 리스트 출력
for i in range(n):
    print(num1[i], result[i])
