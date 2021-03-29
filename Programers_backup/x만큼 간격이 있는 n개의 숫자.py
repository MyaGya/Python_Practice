def solution(x, n):
    return [i for i in range(x,n*x,x)] + [x*n] if x !=0 else [0] * n