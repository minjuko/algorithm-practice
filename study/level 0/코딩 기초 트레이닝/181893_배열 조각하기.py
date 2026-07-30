def solution(arr, query):
    for idx, val in enumerate(query):
        if idx % 2 == 0:
            arr = arr[:val + 1]
        else:
            arr = arr[val:]

    return arr