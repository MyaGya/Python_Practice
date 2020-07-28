#1208
for test_case in range(1,11):
    n = int(input())
    data = list(map(int, (input().split())))


    for _ in range(n):
        data.sort()
        if data[0] ==data[99]: break;
        else:
            data[0] += 1
            data[99] -= 1
    data.sort()
    print("#{0} {1}".format(test_case, data[99]-data[0]))

