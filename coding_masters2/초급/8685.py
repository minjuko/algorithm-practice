a = input()
b = input()
c = int(input())

r = (10 - c) % 10

candidates = []

for i in range(100):
    xx = str(i).zfill(2) if i < 10 else str(i)
    xx = a + xx + b

    A = sum(int(xx[j]) for j in range(len(xx)) if j % 2 == 0)
    B = sum(int(xx[j]) for j in range(len(xx)) if j % 2 == 1)

    if r == (2 * B + A) % 10:
        candidates.append(i)

results = ['X'] * 5

for i in candidates:
    if 11 <= i <= 15:
        results[0] = 'O'
    elif 21 <= i <= 22:
        results[1] = 'O'
    elif 31 <= i <= 51:
        results[2] = 'O'
    elif 81 <= i <= 86:
        results[3] = 'O'
    elif i == 71:
        results[4] = 'O'

print("".join(results))
