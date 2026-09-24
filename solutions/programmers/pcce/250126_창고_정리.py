def solution(storage, num):
    cleaned_storage = []
    cleaned_num = []

    # 1. 같은 물건끼리 수량 합치기
    for i in range(len(storage)):
        if storage[i] in cleaned_storage:
            # 이미 저장된 물건이면 해당 위치의 수량 증가
            pos = cleaned_storage.index(storage[i])
            cleaned_num[pos] += num[i]
        else:
            # 처음 나온 물건이면 새로 추가
            cleaned_storage.append(storage[i])
            cleaned_num.append(num[i])

    # 2. 수량이 가장 많은 물건의 위치 찾기
    max_index = 0

    for i in range(1, len(cleaned_num)):
        if cleaned_num[i] > cleaned_num[max_index]:
            max_index = i

    # 3. 가장 개수가 많은 물건 이름 반환
    return cleaned_storage[max_index]

print(solution(["pencil", "pencil", "pencil", "book"]	, [2, 4, 3, 1]))
# 위 출력 결과 "pencil" 놔야함 개수가 가장 많은 물건의 이름 return