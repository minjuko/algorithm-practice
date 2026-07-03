# 전화번호 입력
# 010-xxxx-xxxx 형태인지 판별

s = input()
if s[:4] == '010-' and s[8] == '-' and len(s) == 13:
    print('valid')
else:
    print('invalid')