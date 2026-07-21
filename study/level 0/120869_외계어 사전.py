def solution(spell, dic):
    # 단어를 하나씩 꺼내서 비교 (정렬)
    for word in dic:
        if sorted(spell) == sorted(word):
            return 1
    return 2