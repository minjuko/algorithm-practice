# 시간 구간 다중 업데이트 다중 합

n = int(input())
info = list(list(input().split()) for _ in range(n))

def solution(n, info):
    T = [0] * 3600
    answer = []
    for a in info:
        if a[0] == '1':
            for i in range(trans_sec(a[1]), trans_sec(a[2])):
                T[i] += 1
        else:
            answer.append(T[trans_sec(a[1])])
    for ans in answer:
        print(ans)

def trans_sec(t):
    return int(t[:2])*60 + int(t[3:])

solution(n, info)