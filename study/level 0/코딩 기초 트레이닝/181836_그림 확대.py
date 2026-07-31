def solution(picture, k):
    answer = []
    # 각 문자를 가로로 k번 반복 + 각 행을 세로로 k번 반복
    for row in picture:
        plus_row = ""

        for char in row:
            plus_row += char * k

        for _ in range(k):
            answer.append(plus_row)

    return answer