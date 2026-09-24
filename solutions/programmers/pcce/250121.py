def solution(data, ext, val_ext, sort_by):
    # ext값이 val_ext보다 작은 데이터를 뽑아 sort_by 해당 값 기준으로 오름차순 정렬
    answer = []
    dict = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3,
    }
    # 기준이 되는 값
    ext_index, sort_index = dict[ext], dict[sort_by]

    for info in data:
        if info[ext_index] < val_ext:
            answer.append(info)
    # sort_by 기준 정렬
    answer.sort(key=lambda info: info[sort_index])

    return answer