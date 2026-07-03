# 학생 이름 찾기 

A = list(input().split()) # 학생 이름 목록 A
B = list(input().split()) # 학생 이름 목록 B

def Solution(A, B):
    D = {} # 딕셔너리 key: 이름, value: 출현 횟수 
    for b in B:
        if b in D:
            D[b] += 1
        else:
            D[b] = 1
    
    answer = []
    for a in A:
        if a not in D:
            answer.append(a)
    answer.sort()
    for ans in answer:
        print(ans)








        
Solution(A, B)

