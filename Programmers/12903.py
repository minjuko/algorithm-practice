# 가운데 글자 가져오기

# 단어의 가운데 글자 반환
# 짝수라면 가운데 두글자 반환 0 1 2 3

def solution(s):
    answer = ''
    mid = len(s) // 2 - 1
    if len(s) % 2 == 0: # 짝수
        answer += s[mid:mid+2]
    else:
        answer += s[mid+1]
    return answer

# 다른 풀이
#  return str[(len(str)-1)//2 : len(str)//2 + 1]
