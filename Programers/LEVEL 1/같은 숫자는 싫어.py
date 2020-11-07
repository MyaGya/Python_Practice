def solution(arr):
    ret = []
    for d in arr:
        if not ret:
            ret.append(d)
        if ret[-1] != d:
            ret.append(d)
    return ret

print(solution([1,1,3,3,0,1,1]	))