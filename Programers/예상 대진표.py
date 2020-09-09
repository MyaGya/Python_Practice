def solution(n,a,b):
    ret = 0
    if a>b:
        a,b = b,a
    while a != b :
        a = (a+1)//2 if a != 0 else 0
        b = (b+1)//2
        ret += 1
    return ret

print(solution(8,4,7))