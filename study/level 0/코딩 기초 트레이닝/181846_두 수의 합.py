def solution(a, b):
    # 오른쪽 자릿수부터 직접 덧셈
    answer = []

    i, j = len(a) - 1, len(b) - 1
    carry = 0

    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            digit_a = int(a[i])
        else:
            digit_a = 0

        if j >= 0:
            digit_b = int(b[j])
        else:
            digit_b = 0

        total = digit_a + digit_b + carry

        answer.append(str(total % 10))
        carry = total // 10

        i -= 1
        j -= 1

    return "".join(reversed(answer))