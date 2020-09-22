def solution(n, s):
    ret = []
    if n>s:
        return [-1]
    for share in range(n,0,-1):
        ret.append(s//share)
        s -= s//share
    return sorted(ret)