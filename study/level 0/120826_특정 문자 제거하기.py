def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i != letter:
            answer += i
    return answer
# 간단한 풀이
# return my_string.replace(letter, '')