# 오리 농법

n = int(input())
# n*n 밭
graph = [list(map(int, input().split())) for _ in range(n)]

# 0은 빈 땅, 1은 작물, 2는 잡초
# 
answer = 0