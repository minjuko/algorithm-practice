def solution(id_pw, db):
    answer = "fail"
    for user_id, user_pw in db:
        if user_id == id_pw[0]:
            if user_pw == id_pw[1]:
                answer = "login"
            else:
                answer = "wrong pw"
            break
    return answer