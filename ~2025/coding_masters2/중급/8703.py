# 일차원 세계의 섬

maps = list(input())
min_ans, max_ans = 0, 0
min_in, max_in = "o", "o"

for i in range(1, len(maps)):
    if maps[i] == "x":
        min_in += min_in[-1]
        if max_in[-1] == 'g':
            max_in += 'o'
        else:
            max_in += 'g'
    else:
        min_in += maps[i]
        max_in += maps[i]
    if max_in[i] == "g" and max_in[i - 1] == "o":
        max_ans += 1
    if min_in[i] == "g" and min_in[i - 1] == "o":
        min_ans += 1

print(min_ans)
print(max_ans)