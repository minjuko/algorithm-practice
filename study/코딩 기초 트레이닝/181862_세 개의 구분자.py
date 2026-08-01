def solution(myStr):
    import re

    answer = [ch for ch in re.split('[abc]', myStr) if ch]

    if not answer:
        return ["EMPTY"]
    else:
        return answer