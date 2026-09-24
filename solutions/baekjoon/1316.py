# 그룹 단어 체커
# 그룹 단어: 각 문자가 모두 연속해서 나타나는 경우

n = int(input())
words = list(input() for _ in range(n))

for word in words:
    for i in range(len(word)-1):
        if word[i] != word[i+1]: # 다음 글자와 다르면 뒤에 해당 문자가 등장하는지 확인
            if word[i] in word[i+1:]:
                n -= 1
                break
print(n)