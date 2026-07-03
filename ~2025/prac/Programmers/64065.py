# 튜플
def solution(s):
    answer = []
    s = s[2: -2] # 맨 처음, 마지막 괄호 빼기
    s = s.split("},{")
    s.sort(key=len)
    for i in s:
        i = i.split(",")
        # 원소 하나씩 꺼내 있는지 확인
        for j in i:
            if not int(j) in answer:
                answer.append(int(j))
    return answer