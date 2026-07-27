def solution(sides):
    answer = 0
    sides.sort()

    # 나머지 한 변이 가장 긴 변
    for i in range(sides[1] + 1, sum(sides)):
        answer += 1
    # for문 개선 >>
    # len(range(sides[1]+1, sum(sides)))

    # 나머지 한 변이 가장 긴 변이 아님
    for i in range(sides[1] - sides[0] + 1, sides[1] + 1):
        answer += 1
    return answer

# 간단한 풀이
# def solution(sides): return 2 * min(sides) - 1