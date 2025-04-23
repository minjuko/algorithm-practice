# 두 배열의 원소 교체
# 최대 k번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 a의 모든 원소의 합의 최댓값 출력
# 바꿔치기 연산 : 각 배열의 원소 하나씩 골라 서로 바꾸는 것

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 오름차순, b는 내림차순 정렬
# 인덱스 순으로 비교하면서 a의 원소가 b보다 작을 때만 교체 진행
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))


