# 이진 변환 반복하기

# x의 모든 0 제거
# x의 길이를 c라고 하면 x를 c를 2진법으로 변환
# 1이 될 때까지 이진 변환

def solution(s):
    cnt = 0 # 변환 횟수
    zero = 0 # 제거된 0의 개수

    while s != '1': # 1이 될 때까지
        zero += s.count('0') # 0 모두 제거하여 카운트
        s = bin(s.count('1'))[2:] # 2진법으로 변환하여 0b 제거
        cnt += 1
    return [cnt, zero]