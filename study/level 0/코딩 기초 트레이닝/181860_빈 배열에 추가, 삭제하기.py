def solution(arr, flag):
    X = []

    for num, val in zip(arr, flag):
        if val:
            X.extend([num] * (num * 2))
        else:
            del X[-num:]

    return X