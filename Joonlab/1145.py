# 시간 구간 다중 업데이트 단일 합

n = int(input())
A = list(list(input().split()) for _ in range(n))

# hh:mm:ss 형식의 시간을 초로 변환
def trans_time(t):
    return int(t[:2])*3600 + int(t[3:5])*60 + int(t[6:])

def solution(n, A):
    T = [0] * 24*60*60
    answer = 0
    for a in A:
        if a[0] == '1':
            T[trans_time(a[1])] += 1
            T[trans_time(a[2])] -= 1
        else:
            for time in range(1, 24*60*60):
                T[time] += T[time-1]
            answer += sum(T[trans_time(a[1]):trans_time(a[2])])
    return answer

print(solution(n, A))