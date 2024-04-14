# 최솟값 만들기

# 두 수 곱하는 과정을 배열 길이 만큼 반복 -> 누적값 최소로

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for a, b in zip(A, B):
        answer += a * b
    return answer