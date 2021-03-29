def solution(x):
    data = list(map(int,list(str(x))))
    return True if int(x) % sum(data) == 0 else False