def solution(s):
    answer = 0
    tmp = s.split()
    for index, value in enumerate(tmp):
        if value != "Z":
            answer += int(value)
        else:
            answer -= int(tmp[index-1])
    return answer

# 이전 값 저장으로 풀기
# def solution(s):
#     answer = 0
#     previous = 0

#     for value in s.split():
#         if value == "Z":
#             answer -= previous
#         else:
#             previous = int(value)
#             answer += previous

#     return answer