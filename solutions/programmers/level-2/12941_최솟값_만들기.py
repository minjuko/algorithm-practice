# 최솟값 만들기

# 배열 A, B에서 두 수를 뽑아 곱하는 과정을 배열의 길이만큼 반복 -> 누적하여 합
# 최종 누적 값을 최소로 만들기

# A의 작은 값을 B의 큰 값과 곱하면 최소가 된다.

def solution(A, B):
    answer = 0
    A.sort() # 오름차순
    B.sort(reverse=True) # 내림차순

    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer

# 다른 풀이
# return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])