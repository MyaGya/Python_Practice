from itertools import permutations
from collections import deque

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def solution(n, k):
    k -= 1 # 0번부터 값이 있으므로 예측 시작
    fac = factorial(n) # 모든 경우의 수
    tmp = deque()
    for i in range(n, 1,-1): # n개의 숫자중에 선택 할 수 있음
        value, remain = divmod(k, factorial(i-1))
        tmp.append(value)
        k = remain
    # 결과 계산
    tmp.append(0) # 마지막 수 삽입(1가지 경우의 수에서 하나를 선택하므로 무조건 0번을 선택한다
    reference = [i+1 for i in range(n)]
    ret = []
    while tmp:
        ret.append(reference.pop(tmp.popleft()))
    return ret


print(solution(3,5))