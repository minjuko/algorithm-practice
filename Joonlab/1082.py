# 특정 대문자를 소문자로 바꾸기

A = input() # 문자열 A
B = list(map(str, input().split())) # 문자 목록 B

def Solution(A, B):
    # B의 대문자가 A에 포함되어 있으면 소문자로 치환 
    for b in B:
        if b in A:
            A = A.replace(b, b.lower())
    return A

print(Solution(A, B))