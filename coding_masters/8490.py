# 내 이름이 적힌 번호 찾기

n, k = input().split() # 이름 수, 영덕의 영어 이름
names = list(input().split())

for i in range(int(n)):
    if names[i] == k:
        print(i + 1)
        break