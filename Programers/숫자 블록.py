# 소수 탐색의 원리와 동일

import math
def solution(begin, end):
    ret = []
    for i in range(begin,end+1):
        if i < 2:
            ret.append(0)
            continue
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                ret.append(i//j)
                break
        else:
            ret.append(1)
    return ret


print(solution(11,20))