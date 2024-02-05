# 더하기 사이클
n = int(input())

# n의 사이클 길이 구하기

answer = 0 # 사이클 길이
tmp = n

while True:
    # 26
    a = tmp//10 # 2
    b = tmp%10 # 6
    c = (a+b)%10 # 2+6 = 8
    tmp = b*10 + c # 68
    answer += 1 # 사이클 +1

    if tmp == n: # 처음 입력한 수로 돌아오면 종료
        break
print(answer)