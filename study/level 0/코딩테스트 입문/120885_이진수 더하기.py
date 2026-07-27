def solution(bin1, bin2):
    # 2진수를 10진수로 변환하여 덧셈 -> 다시 2진수로 변환
    # [2:] >> 접두사 0b 제거
    answer = bin(int(bin1, 2) + int(bin2, 2))[2:]
    return answer