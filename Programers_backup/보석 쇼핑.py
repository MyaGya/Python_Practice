'''
1회차
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


print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
'''

from collections import defaultdict
def solution(gems):
    n = len(set(gems))
    my_gem = defaultdict(int)
    L = R = 0
    ret = []
    flag = False
    while R < len(gems):
        if len(my_gem) < n:         # 보석이 아직 모자란 경우
            my_gem[gems[R]] += 1
        while len(my_gem) == n:
            my_gem[gems[L]] -= 1
            if my_gem[gems[L]] == 0:
                del my_gem[gems[L]]
            L += 1
            flag = True
        if flag:
            ret.append([L,R+1])  # 값 보정
            flag = False
        R += 1

    MAX = [0,100001]
    for data in ret:
        if data[1] - data[0] < MAX[1]-MAX[0]:
            MAX = data
    return MAX


print(solution(["AA", "AB", "AC", "AA", "AC"]))