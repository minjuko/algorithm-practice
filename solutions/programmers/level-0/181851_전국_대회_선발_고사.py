def solution(rank, attendance):
    students = []

    for i in range(len(rank)):
        if attendance[i]:
            students.append(i)

    students.sort(key=lambda i: rank[i])

    a, b, c = students[:3]

    return 10000 * a + 100 * b + c