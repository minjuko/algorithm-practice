def solution(n):
    # 1부터 n까지 먼저 나머지가 1이 되는 수를 찾으면 return
    for x in range(1, n+1):
        if n % x == 1:
            return x