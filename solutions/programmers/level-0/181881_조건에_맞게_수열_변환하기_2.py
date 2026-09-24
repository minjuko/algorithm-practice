def solution(arr):
    answer = 0

    while True:
        tmp = []  # arr(x+1)

        for num in arr:
            if num >= 50 and num % 2 == 0:
                tmp.append(num // 2)
            elif num < 50 and num % 2 == 1:
                tmp.append(num * 2 + 1)
            else:
                tmp.append(num)

        if arr == tmp:
            return answer

        # 1번 반복한 값 저장 후 +1
        arr = tmp
        answer += 1