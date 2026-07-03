# 문자열 복원

s = input()
tmp = len(s) - 1
answer = ''
while tmp>=0:
     if s[tmp] == '0':
         answer += chr(64 + int(s[tmp-2:tmp]))
         tmp -= 3
     else:
         answer += chr(64 + int(s[tmp]))
         tmp -= 1

answer = answer[::-1].lower()
print(answer)

