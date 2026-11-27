# 위에서 아래로
# 수열 내림차순 정렬하기

n = int(input()) # 수열 개수 n
# n개의 정수 수열을 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

# 정렬 결과 출력하기
for i in array:
    print(i, end=(' '))