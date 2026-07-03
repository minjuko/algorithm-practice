# 부가가치세

price = int(input())
vat = int(0.1 * price/(1.1))
diff = price - vat

if int(diff * 0.1) != vat:
    print(-1)
    exit()

print(diff, vat)
