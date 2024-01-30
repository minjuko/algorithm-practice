# 핸드폰 번호 가리기

# 전화번호 뒷 4자리 제외한 숫자 모두 *로 바꾸기

def solution(phone_number):
    phone_number = list((str(phone_number)))
    for i in range(0, len(phone_number) - 4):
        phone_number[i] = "*"
    return ''.join(phone_number)

# 다른 풀이
# return "*"*(len(s)-4)+s[-4:]