#백만장자 프로젝트


T = int(input())

for test_case in range (1 , T+1):
    N = int(input())
    #입력값
    data = list(map(int, (input().split())))
    #최종값
    total = 0
    MAX = data[N-1]
    large = N
    for i in range(N-1, -1,-1):
        #살 수 있는가?
        if(data[i] <= MAX):
            total += MAX - data[i]
        else:
            MAX = data[i]
    print("#{0} ".format(test_case) + str(total))
    total = 0
