def solution(n):
    # 10진법 -> 3진법 : 0이 될 때까지 3으로 나누며 나머지를 문자열에 차례대로 붙이기
    # 3진법 -> 10진법 : int(string, 3) 함수로 변환

    # 1. 3진법으로 변환 + 뒤집기
    # 만약 안뒤집는 경우 마지막에 슬라이싱 [::-1]
    converted = ""
    while n > 0:
        n, remainder = divmod(n, 3)
        converted += str(remainder)

    # 2. 10진법으로 다시 변환
    return int(converted, 3)