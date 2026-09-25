def solution(n):
    return [int(i) for i in str(n)][::-1]

    # 다른 풀이 - map
    # return list(map(int, str(n)[::-1]))
