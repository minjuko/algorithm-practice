# IoU

def iou(rectangles):
    max_iou = 0
    max_iou_pair = None

    for i in range(len(rectangles)):
        x_i, y_i, w_i, h_i = rectangles[i]
        for j in range(i + 1, len(rectangles)):
            x_j, y_j, w_j, h_j = rectangles[j]

            # 두 직사각형이 겹치는 경우
            if x_j >= x_i + w_i or y_j >= y_i + h_i or x_i >= x_j + w_j or y_i >= y_j + h_j:
                continue

            # 겹치는 영역의 너비와 높이
            w_tmp = [(x_i + w_i - x_j), (x_j + w_j - x_i)]
            w_tmp = w_tmp + [w_i] if x_i >= x_j and x_i + w_i <= x_j + w_j else w_tmp
            w_tmp = w_tmp + [w_j] if x_j >= x_i and x_j + w_j <= x_i + w_i else w_tmp
            w_tmp = list(filter(lambda x: x > 0, w_tmp))

            h_tmp = [(y_i + h_i - y_j), (y_j + h_j - y_i)]
            h_tmp = h_tmp + [h_i] if y_i >= y_j and y_i + h_i <= y_j + h_j else h_tmp
            h_tmp = h_tmp + [h_j] if y_j >= y_i and y_j + h_j <= y_i + h_i else h_tmp
            h_tmp = list(filter(lambda y: y > 0, h_tmp))

            # 겹치는 영역의 넓이
            w, h = min(w_tmp), min(h_tmp)
            interset = w * h

            # IoU 계산
            iou = interset / (w_i * h_i + w_j * h_j - interset)

            # 현재까지의 최대 IoU 값보다 크면 갱신
            if iou > max_iou:
                max_iou = iou
                max_iou_pair = (i + 1, j + 1)

    return max_iou_pair if max_iou_pair is not None else (1, 2)

n = int(input())
info = []
for _ in range(n):
    x, y, w, h = map(int, input().split())
    info.append((x, y, w, h))

answer = iou(info)
print(*answer)
