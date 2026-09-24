from datetime import timedelta

# 시간 문자열 -> timedelta 변환
def get_time(k):
    min = int(k[0])
    sec = int(k[1])
    return timedelta(minutes=min, seconds=sec)

# 10초 후로 이동
def move_next():
    global pos_time, video_time
    pos_time += timedelta(seconds=10)
    if pos_time > video_time:
        pos_time = video_time

# 10초 전으로 이동
def move_prev():
    global pos_time
    if pos_time.total_seconds() < 10:
        pos_time = timedelta(seconds=0)
    else:
        pos_time -= timedelta(seconds=10)

# 오프닝 스킵
def skip():
    global pos_time, op_start_time, op_end_time
    if op_start_time <= pos_time <= op_end_time:
        pos_time = op_end_time


def solution(video_len, pos, op_start, op_end, commands):
    global pos_time, video_time, op_start_time, op_end_time

    video_time = get_time(video_len.split(":"))
    pos_time = get_time(pos.split(":"))
    op_start_time = get_time(op_start.split(":"))
    op_end_time = get_time(op_end.split(":"))

    skip()

    for command in commands:
        if command == "prev":
            move_prev()
        else:
            move_next()
        skip()

    total = int(pos_time.total_seconds())
    min, sec = divmod(total, 60)
    answer = f"{min:02}:{sec:02}"

    return answer