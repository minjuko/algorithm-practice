def solution(array):
    # 주의:오름차순 정렬 후 인덱스 값을 저장하면 원본과 인덱스 값이 달라짐
    answer = [max(array), array.index(max(array))]
    return answer