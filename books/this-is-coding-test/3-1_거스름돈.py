# [그리디 알고리즘] 거스름돈
# 가장 큰 화폐 단위부터 돈을 거슬러 준다.

n = int(input()) # n: 거슬러 줘야 할 돈
coin_type = [500, 100, 50, 10] # 화폐 단위 큰 순서대로
result = 0 # 거슬러 줘야 할 동전의 최소 개수

for coin in coin_type:
    result += n // coin # 거슬러 준 동전 수 추가
    n %= coin # n 갱신

print(result)
