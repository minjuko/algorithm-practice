# 달리기 경주

# 이름이 불리면 해당 선수와 바로 앞 선수의 위치가 바뀜
# 경주 종료 후 등수 순서 구하기

def solution(players, callings):
    # dic_player = {선수 이름: 등수} 딕셔너리 저장
    dic_player = {player: rank for rank, player in enumerate(players)}
    for calling in callings:
        rank = dic_player[calling] # 불리는 선수의 등수
        players[rank], players[rank-1] = players[rank-1], players[rank] # 위치 바꾸기
        # 등수 갱신
        dic_player[players[rank]] = rank
        dic_player[players[rank-1]] = rank - 1
    return players

# 시간 초과가 나지 않으려면 딕셔너리 사용
