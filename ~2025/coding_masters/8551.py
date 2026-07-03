# 치팅 검사

words = input().rstrip()
n = len(words) // 2

def cheat(start):
    return words[start:start + n] == words[:start] + words[start + n:]

start, end = 0, len(words) - n

while start < end:
    if cheat(start):
        print('YES')
        print(words[start:start + n])
        exit()
    elif cheat(end):
        print('YES')
        print(words[end:end + n])
        exit()

    start += 1
    end -= 1

print('NO')
