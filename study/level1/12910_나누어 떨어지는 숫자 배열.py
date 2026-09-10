def solution(arr, divisor):
    result = []
    for element in arr:
        if element % divisor == 0:
            result.append(element)

    result.sort()
    return result if result else [-1]