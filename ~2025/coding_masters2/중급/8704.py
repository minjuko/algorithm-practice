# 나이트 자리 바꾸기

board = [list(input()) for _ in range(3)]
if board[1][1] == '0':
    print("possible")
else:
    print("impossible")