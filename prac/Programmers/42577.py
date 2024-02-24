# 전화번호 목록

# 어떤 번호가 다른 번호의 접두어인 경우가 있는지 판별

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
    return answer