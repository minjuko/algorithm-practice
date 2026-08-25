def solution(cards1, cards2, goal):
    idx1, idx2 = 0, 0

    for word in goal:
        # 1.cards1의 현재 단어와 일치
        if idx1 < len(cards1) and cards1[idx1] == word:
            idx1 += 1
        # 2.cards2의 현재 단어와 일치
        elif idx2 < len(cards2) and cards2[idx2] == word:
            idx2 += 1
        # 3. 둘 다 일치 X
        else:
            return "No"

    return "Yes"