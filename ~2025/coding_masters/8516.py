# 문서 통계

n = input() # 문서 내용

# 공백포함 글자 수
print(len(n))

# 공백제외 글자 수
print(len(n.replace(' ', '')))

# 단어 수
print(len(n.split()))
