class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setData(self, first, second):
        pass


a = FourCal(1, 2)
print(type(a))

print(0 / 10)


# 클래스로 예외 지정시키기
class myError(Exception):
    pass


def say_nick(nick):
    if nick == "바보":
        raise myError()
    print(nick)


while (True):

    tmp = input("입력 : ")
    try:
        say_nick(tmp)
    except myError:
        print("허용되지 않는 별명입니다")

