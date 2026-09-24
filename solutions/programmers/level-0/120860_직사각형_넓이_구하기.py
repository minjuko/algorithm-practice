def solution(dots):
    # x/y좌표의 최댓값과 최솟값의 차이가 가로/세로의 길이
    x_values, y_values = [], []

    for x, y in dots:
        x_values.append(x)
        y_values.append(y)

    w = max(x_values) - min(x_values)
    h = max(y_values) - min(y_values)

    return w * h

# 간단한 풀이
# return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])