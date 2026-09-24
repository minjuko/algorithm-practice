def solution(A, B):
    answer = 0  # 밀어야 하는 최소 횟수

    for i in range(len(A)):
        if A == B:
            return answer
        else:
            B = B[1:] + B[0]
            answer += 1
    return -1  # B가 되지 않으면 -1 반환