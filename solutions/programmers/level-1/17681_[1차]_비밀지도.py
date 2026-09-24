def solution(n, arr1, arr2):
    # 전체지도에서 공백이려면 두 지도 모두 공백, 한 곳이라도 벽이면 전체 지도에서도 벽
    result = []
    for a, b in zip(arr1, arr2):
        # 1. OR 연산 후 이진수 변환 (접두사 0b 제거)
        binary = bin(a | b)[2:]
        # 2. n에 맞게 앞부분을 '0'으로 채우기
        binary = binary.zfill(n)
        #3. 1 -> '# 0 -> ' '
        row = binary.replace('1', '#').replace('0', ' ')
        result.append(row)

    return result
