S = input()

def solution(S):
    T = ''
    i = 0
    while i < len(S):
        if S[i] not in {'a', 'A'}:
            T += S[i]
            i += 1
            continue

        # 연속된 문자열 찾기
        j = i + 1
        while j < len(S) and (S[j] == 'a' or S[j] == 'A'):
            j += 1

        # 연속된 문자열이 2번 이상이면 'a'로 치환
        if j - i >= 2:
            T += 'a'
        else:
            T += S[i:j]

        i = j

    print(T)

solution(S)
