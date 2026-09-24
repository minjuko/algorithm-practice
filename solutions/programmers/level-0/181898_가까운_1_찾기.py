def solution(arr, idx):
    answer = []
    for i in len(arr):
        if i >= idx and arr[i] == 1:
            answer.append(i)

    if not answer:
        return -1
    return min(answer)