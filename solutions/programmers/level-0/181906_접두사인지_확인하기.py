def solution(my_string, is_prefix):
    arr = []

    # 접두사 저장
    for i in range(1, len(my_string)):
        arr.append(my_string[:i])

    if is_prefix in arr:
        return 1
    else:
        return 0