from collections import deque
from collections import defaultdict
def solution(gems):

    n = len(set(gems)) # 보석의 수
    my_gems = deque() # 가지고 있는 보석
    my_gems_count = defaultdict(int)
    ans = []
    L = R = 0
    i=0
    while True:
        if len(my_gems_count) < n: # 보석의 수가 작을 경우
            if R >= len(gems):
                break
            my_gems.append(gems[R])
            my_gems_count[gems[R]] += 1
            R += 1 # 보석을 계속 늘린다
        else: # 보석의 수가 n과 같으므로 모든 보석을 얻은 경우
            ans.append([L,R-1])
            L += 1
            gem_name = my_gems.popleft()
            my_gems_count[gem_name] -= 1 # 보석의 크기가 0이된다면 보석을 삭제한다
            if my_gems_count[gem_name] == 0: #
                del my_gems_count[gem_name]
    ret = sorted(ans,key= lambda x:(x[1]-x[0]))[0]
    return [ret[0]+1,ret[1]+1]


print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
))