User
# 문자열 복사

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