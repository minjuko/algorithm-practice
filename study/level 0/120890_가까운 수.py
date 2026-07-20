def solution(array, n):
    array.sort()
    # lambda식 > array의 각 원소를 (n-x)값으로 비교하고, 이 값이 가장 작은 원소 반환
    answer = min(array, key=lambda x : abs(n-x))
    return answer