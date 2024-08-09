# 직선으로 땅 나누기

n = int(input())
answer = 0

while True:
    if (answer*(answer+1))//2 >= n-1:
        print(answer)
        break
    answer += 1
