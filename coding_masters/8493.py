# 사전 만들기

n = int(input())
words = [input() for _ in range(n)]

# 길이 짧은 순 -> 같으면 사전순
words.sort(key=lambda x: (len(x), x))

set_words = set() # 출력한 단어
for word in words:
    if word not in set_words:
        print(word)
        set_words.add(word)
