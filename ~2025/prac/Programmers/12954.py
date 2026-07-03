# x만큼 간격이 있는 n개의 숫자

# x부터 x씩 증가하는 숫자 n개 리스트 구하기
def solution(x, n):
    answer = []
    for i in range(1, n+1): # n개
        answer.append(x*i)
    return answer