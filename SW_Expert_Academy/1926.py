#간단한 369 게임


n = int(input())

for s in range(1, n+1):
    value = s
    flag = False
    while s > 0:
        tmp = s % 10
        s = s // 10
        if tmp % 3 == 0 and tmp > 0:
            print("-", end="")
            flag = True
        else:
            pass
    #True : 3,6,9
    if flag:
        print(" ", end="")
    else:
        print("{0}".format(value), end=" ")

