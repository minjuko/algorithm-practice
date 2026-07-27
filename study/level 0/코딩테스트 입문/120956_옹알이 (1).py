# 옹알이 (1)
def solution(babbling):
    answer = 0
    prons = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in prons:
            i = i.replace(j, " ")
        if i.strip() == "":
            answer += 1
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))