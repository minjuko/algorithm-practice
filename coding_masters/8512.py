# 예비군 훈련

a, b, c, d = input().split() # 연차, 군별, 동원지정여부, 신분

answer = 0 # 연간 훈련 시간
a = int(a)
if d == "Private":
    if a == 0: # 0년차
        answer = 0
    elif 1 <= a <=4: # 1-4년차
        # 동원지정 육해공군
        if c == "Y":
            answer = 28
        else:
            if b == "ROKAF": # 공군
                answer = 28
            else:
                answer = 32
    elif 5 <= a <= 6: # 5-6년차
        answer = 20
elif d == "Officer":
    if a == 0:
        answer = 0
    elif 1<=a<=6:
        answer = 28
print(answer)