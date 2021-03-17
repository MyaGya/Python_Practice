

# 유용한 방법이니 기억해두도록 하자
from itertools import accumulate
def solution(cookie):
    answer = 0
    for m in range(len(cookie)-1):
        a = set(accumulate(reversed(cookie[:m+1])))
        b = set(accumulate(cookie[m+1:]))
        c = a & b

        if c:
            answer = max(*c, answer)
    return answer

print(solution([1,1,2,3]))