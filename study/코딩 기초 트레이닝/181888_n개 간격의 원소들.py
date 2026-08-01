def solution(num_list, n):
    answer = [num_list[i] for i in range(0, len(num_list), n)]
    return answer

# 다른 풀이
# 슬라이싱 형식 : 리스트[시작:끝:간격]
# return num_list[::n]