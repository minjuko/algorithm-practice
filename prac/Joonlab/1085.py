# 물건값 계산 

n, m = map(int, input().split()) # n : 파는 물건 수, m : 구매하는 물건 수 

# 물건 정보 A 입력 
A = list(list(input().split()) for _ in range(n)) # (물건 이름, 물건 가격) n개 정보 

# 구매 정보 B 입력 
B = list(input().split()) # (물건 이름) 정보 

def solution(n, m, A, B):
    # 딕셔너리 설정 
    D = {}
    for name, cost in A:
        D[name] = int(cost)
    
    answer = 0 # 구매하려는 물건 가격의 합 
    for name in B:
        answer += D[name]
    return answer 

print(solution(n, m, A, B))