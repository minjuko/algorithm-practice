# 요세푸스 문제

# 원을 이룬 n명 사람이 모두 제거될 때까지 k번째 사람 제거
# 제거된 순서 구하기

from collections import deque

n, k = map(int, input().split())
people = deque([i for i in range(1, n+1)]) # n명 담은 큐
result = [] # 순서 기록

while people: # 큐가 빌 때까지
    for _ in range(k-1): # k-1번째 사람까지 뒤로 보내기
        people.append(people.popleft())
    result.append(people.popleft()) # k번째 사람 제거

print('<' + ', '.join(map(str, result)) + '>') # 결과 출력