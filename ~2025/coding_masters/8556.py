# 어묵과 파르페

words = list(map(str, input().split('F')))
len_word = [len(word) for word in words if word]
if len_word:
    print(sum(len_word)-max(len_word))
else:
    print(0)
