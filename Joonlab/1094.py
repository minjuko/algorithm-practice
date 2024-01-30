from collections import deque

n = int(input())
S = list(list(map(int, input().split())) for _ in range(n))

def solution(n, S):
    answer = [[] for _ in range(3)]
    q = deque()

    for info in S:
        if info[0] == 1:
            q.append((info[1], info[2]))
        else:
            a, b = q.popleft()
            if b == info[1]:
                answer[0].append(a)
            else: 
                answer[1].append(a)
    while len(q) > 0:
        a, b = q.popleft()
        answer[2].append(a)

    
    for i in range(3):
        answer[i].sort()
    for ans in answer:
        if len(ans) == 0:
            print('None')
        else:
            for x in ans:
                print(x, end=' ')
            print()
            
solution(n, S)

