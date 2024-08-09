# 최대공약수와 최소공배수

def solution(n, m):
    # 최대공약수 (math 함수에도 있음)
    def gcd(a, b):
        while (b > 0):
            a, b = b, a % b
        return a

    # 최소공배수
    def lcm(a, b):
        return a * b / gcd(a, b)

    answer = []
    answer.append(gcd(n, m))
    answer.append(lcm(n, m))
    return answer