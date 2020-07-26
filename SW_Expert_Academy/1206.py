#1026
#테스트케이스는 10으로 고정된다.
T = 10

for test_case in range(1, T+1):
    n = int(input())
    Building1 = list(map(int, input().split()))
    total = 0
    for cur in range(2, n-2):
        look = sorted(Building1[cur-2:cur+3])
        if(look[4] == Building1[cur]):
            total += Building1[cur] - look[3]
    print("#{0} ".format(test_case) + str(total))
    total=0
