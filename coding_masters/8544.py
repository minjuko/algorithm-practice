# 문자열 복사 사태가 벌어졌습니다.
#
# 따라서 현재 모든 사람들이 "문자열 복사"를 할 수 있게 되었습니다.
#
#
#
# 문자열 복사의 과정은 다음과 같습니다.
#
# 먼저, 길이가 N인 원본 문자열에 대해, 1 ≤ k ≤ N인 정수 k를 고릅니다.
#
# 그 뒤, 해당 문자열에서 k개의 연속되는 문자들을 골라 복사하여 각 문자 위치 바로 뒤에 붙여넣습니다.
#
# 예를 들어, 원본 문자열이 "string" 일 때 3개의 연속되는 문자 "tri" 를 골라 복사하면 "sttrriing"이 됩니다.
#
#
#
# 민겸은 문자열 복사를 이용하여 특정한 문자열을 만들려고 합니다.
#
# 민겸은 현재 세 글자의 문자열을 가지고 있습니다.
#
# 민겸이 문자열 복사를 최소 몇 번 해야 목표 문자열을 만들 수 있을지 알려주는 프로그램을 작성하세요.
#
#
# 예제 입력1
#
# NOS
# NNOOOSS
#
# 예제 출력1
#
# 2
#
# 예제 입력2
#
# PPS
# PPPPPSSSSS
#
# 예제 출력2
#
# 3
#
#
# 입력값 설명
#
# 입력은 두 줄로 주어집니다. 첫 번째 줄에 민겸이 원래 가지고 있는 문자열 S1이 주어집니다.
# 두 번째 줄에 민겸이 만들려고 하는 문자열 S2가 주어집니다.
# S1의 길이는 3이며, S2의 길이는 100 이하입니다.
# 두 문자열은 모두 영어 대문자로만 되어 있습니다.
#
# 출력값 설명
#
# 민겸이 문자열 복사를 최소 몇 번 해야 목표 문자열을 만들 수 있는지 출력합니다.
# 만드는 게 가능한 입력만 주어집니다.

s1 = input().strip()
s2 = input().strip()

a, b = 0, 0
stack = []
stack2 = []

while a<3:
    cnt = 1
    while a + cnt < len(s1) and s1[a] == s1[a+cnt]:
        cnt += 1

    cnt2 = 1
    while b + cnt2 < len(s2) and s2[b] == s2[b+cnt2]:
        cnt2 += 1
    stack.append(cnt)
    stack2.append(cnt2)

    a += cnt
    b += cnt2

cnt3 = 0
while stack < stack2:
    if len(stack2) == 3 and stack[1]*2 <= stack2[1]:
        stack = [min(i*2, stack2[j]) if j in (0, 2) else i*2 for j, i in enumerate(stack)]
    else:
        tmp = []
        tmp += [[min(i*2, stack2[j]) if j in (0, 1) else i for j, i in enumerate(stack)]]
        tmp += [[min(i*2, stack2[j]) if j in (1, 2) else i for j, i in enumerate(stack)]]
        tmp += [[min(i*2, stack2[j]) if j == 2 else i for j, i in enumerate(stack)]]
        tmp += [[min(i * 2, stack2[j]) if j == 0 else i for j, i in enumerate(stack)]]
        tmp += [[min(i * 2, stack2[j]) if j == 1 else i for j, i in enumerate(stack)]]

        tmp.sort(reverse=True)
        for k in tmp:
            if not list(filter(lambda x: x[0] < x[1], zip(stack2, k))):
                stack = k
                break
    cnt3 += 1

print(cnt3)