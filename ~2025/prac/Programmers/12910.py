# 나누어 떨어지는 숫자 배열

# 원소 중 divisior로 나누어 떨어지는 값을 오름차순 정렬한 배열 구하기

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    if answer:
        return answer
    else:
        return [-1]