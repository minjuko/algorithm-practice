def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer

# sum 함수 + 리스트 이용하기
# return sum([int(i) for i in str(number)])