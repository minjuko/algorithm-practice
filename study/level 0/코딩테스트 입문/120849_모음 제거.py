def solution(my_string):
    answer = ''
    for str in my_string:
        if str not in ["a", "e", "i", "o", "u"]:
            answer += str
    return answer