# 삽입 정렬 연습
# 특정 데이터를 적절한 위치에 삽입
# 그 앞까지의 데이터는 정렬되어 있다고 가정 (두 번째 데이터부터 시작)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 두 번째 데이터부터 시작
    for j in range(i, 0, -1): # i부터 왼쪽으로 이동하면서 반복
        # 한 칸씩 왼쪽으로 이동, 자신보다 작은 데이터를 만나면 멈춤
        if array[j] < array[j - 1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)