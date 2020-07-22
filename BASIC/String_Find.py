list = ["ABC", "CBD", "AVDBD", "ABCD"]

Result = [s for s in list if s == "ABC"]

print(Result)


# 함수와 전달 값의 비교

def Func(INP):
    print(INP)


INP = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Func(INP)