def solution(M, N):
    # N개의 줄 -> 가위질 N-1
    # 길이가 M인 각 줄을 1씩 나누기 -> M-1 가위질 (*N번)
    answer = (M-1) * N + (N-1)
    return answer