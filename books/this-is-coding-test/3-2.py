# 큰 수의 법칙
# 배열의 크기 n, 숫자가 더해지는 횟수 m, 그리고 k가 주어질 때 큰 수의 법칙에 따른 결과 출력하기
# 조건 1 : 주어진 수를 m번 더하여 가장 큰 수 만들기
# 조건 2 : 배열의 특정 인덱스에 해당하는 수가 연속해서 k번을 초과하여 더해질 수 없음

# 반복되는 수열의 규칙 파악하기 - [가장 큰 수 k개] + [두 번째로 큰 수 1개] 묶음 (길이: k+1)
# 묶음 내 포함된 가장 큰 수의 개수 : (m // (k+1)) * k
# 묶음 계산 후 남은 횟수 동안 가장 큰 수 개수 : m % (k+1)

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
# 가장 큰 수, 두 번째로 큰 수
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += count * first # 가장 큰 수 계산
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)