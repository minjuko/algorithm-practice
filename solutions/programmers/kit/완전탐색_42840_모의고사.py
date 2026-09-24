"""
각 수포자의 찍기 패턴을 적용하여 정답 개수 계산 -> 가장 많이 맞힌 사람 찾기
- 패턴 주기 파악 : 몇 주기로 같은 패턴이 반복되는지
- % 연산자 사용하여 주기를 반복해서 패턴 확인
"""


def solution(answers):
    # 수포자의 찍기 패턴
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]  # 수포자의 정답 개수 저장

    # 정답 배열을 순회하면서 정답 개수 계산
    for i, answer in enumerate(answers):
        if answer == pattern1[i % len(pattern1)]:
            scores[0] += 1
        if answer == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if answer == pattern3[i % len(pattern3)]:
            scores[2] += 1

    # 최고 점수 계산 -> 최고 점수를 받은 사람 찾기(여러 명이면 오름차순)
    max_score = max(scores)
    result = []
    for idx, score in enumerate(scores):
        if score == max_score:
            result.append(idx + 1)  # 사람은 1번부터

    return result