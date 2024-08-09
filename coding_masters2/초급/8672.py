# 수하물
# k개의 가방, 하나의 가방에는 무게 제한을 넘지 않는 하나의 물건만 담기 가능
# 가져갈 수 있는 물건들의 가격의 합의 최댓값 구하기

n, k = map(int, input().split()) # 물건 수, 가방 수

# 물건 정보 (무게, 가격)
items = [list(map(int, input().split())) for _ in range(n)] # 물건 정보
bags = [int(input()) for _ in range(k)] # 가방 정보
answer = 0

items.sort(key=lambda x: x[1], reverse=True)
bags.sort()

for i in range(n):
    if bags:
        for j in bags:
            if items[i][0] <= j:
                answer += items[i][1]
                bags.remove(j)
                break
print(answer)
