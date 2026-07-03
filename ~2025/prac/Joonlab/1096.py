# 단일 항목 선호도 조사

n, m = map(int, input().split()) # n명의 학생, m개의 질의
info = list(input().split()) # n명의 학생의 선호도
question = list(input().strip() for _ in range(m)) # m개의 질의
# 문자열 끝의 개행문자 제거를 위해 strip

def solution(n, m, info, question):
    answer = []
    for q in question:
        if q == '-':
            answer.append(n)
        else:
            cnt = 0
            for i in info:
                if i == q:
                    cnt += 1
            answer.append(cnt)
    for ans in answer:
        print(ans)
solution(n, m, info, question)
