def solution(phone_number):
    # 문자열 길이 - 4 만큼 * 추가 + 뒷자리 4개(-4:)
    # phone_number[:-4] : 처음부터 뒷 4자리 전까지
    # phone_number[-4:] : 끝에서 4번째부터 끝까자ㅣ
    answer = "*"*(len(phone_number)-4) + phone_number[-4:]
    return answer