lt = ["ABC", "CBD", "AVDBD", "ABCD"]

Result = [s for s in lt if s == "ABC"]

print(Result)


# 함수와 전달 값의 비교

def Func(INP):
    print(INP)


INP = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Func(INP)

ling = "1 2"
tmp = map(int, ling.split(" "))

print(tmp)
a, b = list(tmp)
print(a, b)

