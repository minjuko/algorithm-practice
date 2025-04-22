# 성적이 낮은 순서로 학생 출력하기

# n명의 학생 정보 (이름 성적)
# 성적 낮은 순서대로 이름 출력하기

n = int(input()) # 학생 수
# 학생 정보 입력 받아 저장 (성적은 정수형으로)
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

# 성적 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')