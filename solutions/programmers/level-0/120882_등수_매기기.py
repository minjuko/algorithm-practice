def solution(score):
    # 두 점수의 합으로만 비교해도 된다.
    total_scores = [a + b for a, b in score]  # 영어점수 + 수학점수
    # 원본 배열의 순서가 필요하므로 정렬한 배열을 따로 복사
    sorted_scores = sorted(total_scores, reverse=True)  # 성적순의 정렬
    answer = []

    for total in total_scores:
        answer.append(sorted_scores.index(total) + 1)  # 순위 1부터 시작

    return answer