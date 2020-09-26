# 소수 탐색의 원리와 동일

import math
def solution(begin, end):
    ret = []
    set_block = 10**7 # 블록이 깔려있는 위치
    for i in range(begin,end+1):
        if i < 2:
            ret.append(0)
            continue
        for j in range(2,int(math.sqrt(i))+1): # 1일때에는 해당 안되기때문에 2부터 계산한다
            if i % j == 0:
                if i//j > set_block:
                    continue
                ret.append(i//j)
                break
        else:
            ret.append(1)
    return ret


print(solution(11,20))