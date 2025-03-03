# 큰 수의 법칙
# 더 효율적인 풀이 -> 가장 큰 수, 두 번째 큰 수 더해질 때 반복되는 수열 규칙 찾기
# int(m/(k+1))*k + m%(k+1)

n, m, k = map(int, input().split()) # n: 배열의 크기
data = list(map(int, input().split())) # 배열
result = 0 # 가장 큰 수
# 가장 큰 수를 k번 더하기 -> 두 번째로 큰 수 1번 더하기 이것을 반복.
data.sort(reverse=True)
first, second = data[0], data[1] # 가장 큰 수, 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result += count * first + (m-count) * second
print(result)