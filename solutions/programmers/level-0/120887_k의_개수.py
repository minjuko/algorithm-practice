def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        tmp = str(num) # 문자열로 바꿔서 비교
        for num2 in tmp:
            if num2 == str(k):
                answer += 1
    return answer