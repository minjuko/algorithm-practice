def solution(my_string, is_suffix):
    arr = []

    # 모든 접미사 저장
    for i in range(len(my_string)):
        arr.append(my_string[i:])

    if is_suffix in arr:
        return 1
    else:
        return 0