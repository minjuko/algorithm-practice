def solution(box, n):
    # 직육면체 가로세로높이를 n으로 나눈 몫
    answer = ((box[0] // n) * (box[1] // n) * (box[2] // n))
    return answer