# 대문자 제거하기 

A = input() # 문자열 A 

def Solution(A):
    # A에서 대문자 제거 
    B = "" # 문자열 B

    # A에서 소문자인 원소만 B에 추가
    for a in A:
        if a.islower():
            B += a
    return B

print(Solution(A))

# 대문자 판단은 isupper()