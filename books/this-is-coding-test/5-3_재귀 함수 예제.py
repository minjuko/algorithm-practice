def recursive_function():
    print('재귀 함수 호출')
    recursive_function()

recursive_function()

# 실행 시 RecursionError: maximum recursion depth exceeded 오류
# -> 재귀의 최대 깊이 초과. 무한대로 재귀 호출 진행할 수 없음