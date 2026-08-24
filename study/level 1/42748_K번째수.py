def solution(array, commands):
    # i, j, k는 1번째부터 시작하는 기준이므로 이를 고려해야함.
    answer = []
    for command in commands:
        i, j, k = command
        tmp = array[i - 1:j]
        tmp.sort()
        answer.append(tmp[k - 1])

    return answer