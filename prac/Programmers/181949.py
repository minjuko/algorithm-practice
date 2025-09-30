# 대소문자 바꿔서 출력하기

str = input()
result = ''
for alpha in str:
    if alpha.isupper():
        result += alpha.lower()
    else:
        result += alpha.upper()

print(result)