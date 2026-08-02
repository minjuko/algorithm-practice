def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        # numbers의 학생 번호와 score_list의 인덱스 1 차이 
        # our_score에는 numbers와 같은 순서대로 저장
        if our_score[i] == score_list[numbers[i] -1]:
            answer.append("Same")
        else:
            answer.append("Different")
    return answer