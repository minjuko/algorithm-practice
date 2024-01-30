# 배열 다중 업데이트 단일 합

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(list(map(int, input().split())) for _ in range(m)) # 질의

# 1 유형 : i번부터 j번 원소에 k 더하기
# 2 유형 : i번부터 j번 원소의 합 구하기
# 배열 B에는 2 유형이 마지막에 한 번 저장

def solution(n, m, A, B):
    psum = [0] * n # 누적 합 배열

    # 질의 순서대로 처리
    for b in B:
        if b[0] == 1: # 유형 1
            psum[b[1]] += b[3] # i번부터 j번 원소에 k 더하기
            # 누적합 이용
            if b[2] + 1 < n:
                psum[b[2]+1] -= b[3]
        else: # 유형 2
            # 누적합 계산
            for i in range(1, n):
                psum[i] += psum[i-1]
            return sum(psum[b[1]:b[2]+1]) + sum(A[b[1]:b[2]+1]) # i번부터 j번 원소의 합 구하기
print(solution(n, m, A, B))