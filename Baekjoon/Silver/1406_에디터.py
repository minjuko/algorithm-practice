# 에디터

stack1 = list(input())
stack2 = []

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'L' and stack1:
        stack2.append(stack1.pop())
    elif command[0] == 'D' and stack2:
        stack1.append(stack2.pop())
    elif command[0] == 'B' and stack1:
        stack1.pop()
    elif command[0] == 'P':
        stack1.append(command[1])

print(''.join(stack1 + stack2[::-1]))
