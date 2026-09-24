# 식당 입구 대기 줄 

from collections import deque

n = int(input())
A = list(list(map(int, input().split())) for _ in range(n)) 

def solution(n, A):
    answer = [0, 0] # [대기 학생수 최댓값, 맨 뒤 학생 번호]
    q = deque() # 큐 : 대기 중인 학생 번호 저장 

    for i in A:
        if i[0] == 1: # 학생이 도착 -> 대기 중 학생 수 증가 
            q.append(i[1])
            if answer[0] < len(q) or \
                (answer[0] == len(q) and answer[1] > i[1]):
                answer = [len(q), i[1]]
        else:
            q.popleft()
    print(answer[0], answer[1])

solution(n, A)