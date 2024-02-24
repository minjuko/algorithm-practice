# 카펫

# 중앙 노랑, 테두리 갈색 격자 카펫
# 갈색/노란색 격자의 수 -> 카펫 크기 구하기

# 전체 면적 = yellow + brown = width * height
# 노란색 면적 = (width - 2) * (height - 2)
# 갈색 면적 = 2*width + 2*height - 4 (모서리 4칸 제외)

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for x in range(1, total+1): #가능한 w, h 탐색
        if total % x == 0:
            y = total // x
            if x >= y:
                if 2*x + 2*y - 4 == brown:
                    answer.append(x)
                    answer.append(y)
                    break
    return answer
