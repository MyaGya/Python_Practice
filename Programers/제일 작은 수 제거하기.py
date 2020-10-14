def solution(arr):
    delete = min(arr)

    ret = []
    for i in arr:
        if i != delete:
            ret.append(i)
    return ret if ret else [-1]