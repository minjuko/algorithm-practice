# 회색조
def make_gray(color):
    red = int(color[1:3], 16)
    green = int(color[3:5], 16)
    blue = int(color[5:7], 16)

    gray = round((red + green + blue) / 3)
    gray_hex = f'{gray:02X}'

    return f'#{gray_hex * 3}'

color = input().strip()
print(make_gray(color))
