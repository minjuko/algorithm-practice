# 펀드

# 예상 수익 금액 : 상품 기본 금액 + 상품 신용도 * 옵션의 금액의 합
# n개의 옵션 중 정해진 개수의 옵션을 최대 m개까지 적용
# 가능한 최대 예상 수익 금액

a, b = map(int, input().split()) # 상품 기본 금액, 신용도
n, m = map(int, input().split()) # 옵션 수, 최대 적용 가능 옵션 수
options = [int(input()) for _ in range(n)] # 옵션 금액 정보

options.sort(reverse=True)
answer = sum(options[:m])

print(a + b * answer)