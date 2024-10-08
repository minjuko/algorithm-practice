from datetime import timedelta

# 시간 문자열을 timedelta로 변환하는 함수
def get_time(split):
    min = int(split[0])
    sec = int(split[1])
    return timedelta(minutes=min, seconds=sec)

# 10초 후로 이동하는 함수
def move_to_next():
    global pos_time, video_time
    pos_time += timedelta(seconds=10)
    if pos_time > video_time:  # 전체 동영상 시간을 넘어가는 경우
        pos_time = video_time

# 10초 전으로 이동하는 함수
def move_to_prev():
    global pos_time
    if pos_time.total_seconds() < 10:  # 현재 재생위치 10초 전으로 이동하면 0초가 되는 경우
        pos_time = timedelta(seconds=0)
    else:
        pos_time -= timedelta(seconds=10)

# 오프닝 스킵하는 함수
def skip_op():
    global pos_time, op_start_time, op_end_time
    if op_start_time <= pos_time <= op_end_time:
        pos_time = op_end_time

# 메인 로직
def solution(video_len, pos, op_start, op_end, commands):
    global pos_time, video_time, op_start_time, op_end_time

    video_time = get_time(video_len.split(":"))  # 전체 동영상 시간
    pos_time = get_time(pos.split(":"))  # 현재 재생위치
    op_start_time = get_time(op_start.split(":"))  # 오프닝 시작 위치
    op_end_time = get_time(op_end.split(":"))  # 오프닝 끝 위치

    skip_op()  # 오프닝 스킵

    for command in commands:
        if command == "prev":
            move_to_prev()  # 10초 전으로 이동
        else:
            move_to_next()  # 10초 후로 이동
        skip_op()  # 오프닝 스킵

    # 결과를 "mm:ss" 형식의 문자열로 변환
    total_seconds = int(pos_time.total_seconds())
    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes:02}:{seconds:02}"

# 테스트
if __name__ == "__main__":
    print(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"]))
    print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]))
    print(solution("07:22", "04:05", "00:15", "04:07", ["next"]))
    print(solution("30:00", "29:55", "01:00", "01:30", ["next"]))
