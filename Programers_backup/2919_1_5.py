def solution(stones, k):
    zerodata = []
    ans = 1
    flag = False
    while True:
        for i in range(len(stones)):
            stones[i] -= 1
            if(stones[i] == 0):
                zerodata.append(i)
        zerodata.sort()
        for i in range(len(zerodata)-k):
            flag = True
            for j in range(i, i+k-1):
                if zerodata[j] + 1 is zerodata[j+1]:
                    pass
                else:
                    flag = False
                    break;
            if flag:
                break;
        if flag:
            break;
        ans += 1
    return ans

k = int(input())
stones = list(map(int, input().split()))

print(solution(stones, k))