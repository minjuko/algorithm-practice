# 원의 넓이

r = int(input())
answer = r * r * 3.14

# 정수이면 소수부분 출력 X
if answer == int(answer):
    print(int(answer))
else:
    print(answer)
