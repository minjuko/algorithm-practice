# n^2 배열 자르기

# 1. n*n 2차원 배열 만들기
# 2. 1행 1열부터 i행 i열까지 모든 빈 칸을 i로 채우기
# 3. 1행, 2행 ... n행을 잘라내 이어붙인 새 1차원 배열 만들기
# 4. 새 1차원 배열에서 arr[left], arr[left+1], ... arr[right]남기기

# 해당 위치 = (해당 위치를 n으로 나눈 나머지와 몫 중 큰 값) + 1
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(max(i//n, i%n)+1)
    return answer