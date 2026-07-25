def solution(arr, queries):
    answer = []

    for query in queries:
        s, e, k = query[0], query[1], query[2]
        tmp = []

        # k보다 큰 경우 저장
        for i in range(s, e + 1):
            if arr[i] > k:
                tmp.append(arr[i])
        # 가장 작은 값
        if tmp:
            answer.append(min(tmp))
        else:
            answer.append(-1)

    return answer