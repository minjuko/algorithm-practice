# 공부한 시간의 합 

A =  list(input().split()) # 공부시간 목록 문자열 A (00:10 01:50) 시:분

def Solution(A):
    # A의 시간을 분으로 치환
    B = [] # 분으로 치환된 시간 목록 B
    for a in A:
        B.append(int(a[0:2]) * 60 + int(a[3:5]))

    # B의 합을 시:분으로 치환
    total_minutes = sum(B)
    hours = total_minutes // 60
    minutes = total_minutes % 60

    return f"{hours:02d}:{minutes:02d}"

print(Solution(A))