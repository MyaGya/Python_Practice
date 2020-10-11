from math import sqrt
def solution(n):
    n = sqrt(n)
    return (int(n)+1) ** 2 if int(n) == n else -1

