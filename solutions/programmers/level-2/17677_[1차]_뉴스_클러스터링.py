# [1차] 뉴스 클러스터링

# 두 문자열의 유사도 출력 * 65536
# 두 글자씩 끊어 영문자로 된 글자쌍만 유효
# 대소문자 구분 X

from collections import Counter


def solution(str1, str2):
    answer = 0

    # 다중 집합 만들기
    s1 = [str1[i:i + 2].lower() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    s2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]

    if not s1 and not s2:
        return 65536
    c1 = Counter(s1)
    c2 = Counter(s2)
    answer = int(float(sum((c1 & c2).values())) / float(sum((c1 | c2).values())) * 65536)
    return answer