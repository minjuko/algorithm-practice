def solution(todo_list, finished):
    answer = []

    for i in range(len(todo_list)):
        if not finished[i]:  # 마치지 못한 경우
            answer.append(todo_list[i])
    return answer