year = int(input())
age_type = input()

if age_type == "Korea":
    answer = 2030 - year + 1
elif age_type == "Year":
    answer = 2030 - year

print(answer)

# age_type이 "Korea", "Year" 중 하나 -> answer를 미리 초기화하지 않아도 됨.
# 두 조건 중 하낙 반드시 실행됨