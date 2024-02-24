# 평균

n = int(input()) # 과목 수
score = list(map(int, input().split())) # 점수 입력

# 점수/최댓값 * 100

answer = [i/max(score)*100 for i in score]
print(sum(answer)/n)