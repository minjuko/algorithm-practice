import sys

graph = list(map(lambda x: x.strip(), sys.stdin.readlines()))


def solution(arr):
    result = []
    for i in range(len(graph)):
        val = list(filter(lambda x: graph[i][x] == "#", range(len(graph[i]))))
        result += list(map(lambda x: (i, x), val))
    if len(result) != 4: return "NO"
    x, y = result[0]

    if result == [(i, y) for i in range(x, x + 4)] or result == [(x, j) for j in range(y, y + 4)]:
        return "YES"
    if (x, y + 1) in result and (x + 1, y) in result and (x + 1, y + 1) in result:
        return "YES"

    if (x, y + 1) in result and (x, y + 2) in result and (x + 1, y) in result:
        return "YES"
    elif (x, y + 1) in result and (x, y + 2) in result and (x + 1, y + 2) in result:
        return "YES"
    elif (x + 1, y) in result and (x + 1, y + 1) in result and (x + 1, y + 2) in result:
        return "YES"
    elif (x + 1, y - 2) in result and (x + 1, y - 1) in result and (x + 1, y) in result:
        return "YES"
    elif (x + 1, y) in result and (x + 2, y) in result and (x + 2, y + 1) in result:
        return "YES"
    elif (x + 1, y) in result and (x + 2, y) in result and (x + 2, y - 1) in result:
        return "YES"

    if (x + 1, y) in result and (x + 1, y + 1) in result and (x + 2, y + 1) in result:
        return "YES"
    elif (x + 1, y) in result and (x + 1, y + 1) in result and (x + 2, y + 1) in result:
        return "YES"
    elif (x, y + 1) in result and (x + 1, y + 1) in result and (x + 1, y + 2) in result:
        return "YES"
    elif (x, y + 1) in result and (x + 1, y - 1) in result and (x + 1, y) in result:
        return "YES"

    if (x, y + 1) in result and (x, y + 2) in result and (x + 1, y + 1) in result:
        return "YES"
    elif (x, y + 1) in result and (x, y + 2) in result and (x - 1, y + 1) in result:
        return "YES"
    elif (x + 1, y) in result and (x + 1, y + 1) in result and (x + 2, y) in result:
        return "YES"
    elif (x + 1, y) in result and (x + 1, y - 1) in result and (x + 2, y) in result:
        return "YES"

    return "NO"


print(solution(graph))
