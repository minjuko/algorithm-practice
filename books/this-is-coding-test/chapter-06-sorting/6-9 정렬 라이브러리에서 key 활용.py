# key 매개변수 활용
# sorted, sort 이용 시 key 매개변수 입력 가능
# key 값 : 정렬 기준, 하나의 함수

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]
result = sorted(array, key=setting)
# 함수를 바로 정의할 때는 lambda 쓰기
#result = sorted(array, key=lambda data: data[1])
print(result)