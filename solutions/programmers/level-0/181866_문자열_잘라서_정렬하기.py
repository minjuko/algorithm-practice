def solution(myString):
    # x 기준 문자열 자르기, 공백 제외
    myString = [i for i in myString.split("x") if i]
    myString.sort()
    return myString