# 단어 퍼즐

from itertools import permutations

words = [list(input()) for _ in range(6)]
permutate = permutations(range(6), 3)
answer = []

for perm in permutate:
    arr = [words[i] for i in perm]
    arr2 = [words[i] for i in range(6) if i not in perm]

    for i in list(zip(*arr)):
        if list(i) not in arr2:
            break
        else:
            arr2.remove(list(i))
    else:
        answer.append(arr)

answer.sort()
for i in answer[0]:
    print(''.join(i))


