start = int(input())
before = int(input())
after = int(input())

money = start # 첫 달 금액 넣기
month = 1 # + 첫 달

# 70만원까지 모으기
while money < 70:
    money += before
    month += 1
# 100만원까지 모으기
while money < 100:
    money += after
    month += 1

print(month)
