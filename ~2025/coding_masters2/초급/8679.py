# 채터링

n, k = map(int, input().split()) # 문자열 길이, 채터링 입력 횟수
s = input()
answer = ''
for i in s:
    answer += i*k

print(answer)
