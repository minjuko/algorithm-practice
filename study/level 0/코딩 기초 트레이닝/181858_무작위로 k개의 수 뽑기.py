def solution(arr, k):
    answer = []
    select = set()  # 나온 수 저장

    for num in arr:
        if num not in select:
            select.add(num)
            answer.append(num)

        if len(answer) == k:
            break
    # 배열이 k보다 작으면 나머지 값을 -1로 채우기
    return answer + [-1] * (k - len(answer))