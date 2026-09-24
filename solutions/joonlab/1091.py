# 가장 많이 나온 수 찾기 
from collections import Counter

n = int(input())
A = list(map(int, input().split()))

def solution(n, A):
    counts = Counter(A)
    max_count = max(counts.values())
    answer = sorted(num for num, count in counts.items() if count == max_count)
    print(*answer)

solution(n, A)