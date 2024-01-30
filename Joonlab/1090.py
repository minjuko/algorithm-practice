# 비슷한 전화번호 표시 

A = list(input().split()) # 전화번호 문자열 A (여러 개 ) 
B = input() # 전화번호 문자열 B (1개)

def Solution(A, B):
    D = {} # key: 자신을 제외한 전화번호 접두사, value: 출현횟수 
    for a in A:
        for i in range(len(a)-1):
            x = a[:i + 1]
            if x in D:
                D[x] += 1
            else:
                D[x] = 1
    if B in D:
        return D[B]
    else:
        return 0
print(Solution(A, B))
