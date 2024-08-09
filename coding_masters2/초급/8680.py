# 기차와 파리

x, y, z = map(int, input().split()) # 기차 사이 거리, 기차 속도, 파리 속도

answer = ((x*z)//(y*2))
print(answer)