import math
def solution(s):
    s = list(map(int,s.split()))
    MIN = math.inf
    MAX = -math.inf
    for d in s:
        if MIN > d:
            MIN = d
        if MAX < d:
            MAX = d
    return " ".join([str(MIN), str(MAX)])

print(solution("1 2 3 4"))