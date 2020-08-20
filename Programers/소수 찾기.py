# O(전체 배열 * (배열의 길이 * 많은 수 중 배열을 선택하는 경우의 수(해당 숫자마다 소수인지 판별 ) 만큼의 시간이 필요
# O(n * (n * n (소수판별시간))) = n^3
from itertools import permutations
from collections import defaultdict
# 소수 판별
def isPrime(value,visited):

    if visited[value] != 0: # 이미 판별이 끝난 값일 경우
        return False

    for i in range(2, value//2+1):
        if value % i == 0:
            visited[value] = -1
            return False
    visited[value] = 1
    return True
def solution(numbers):
    # init
    visited = defaultdict(int)
    visited[1] = visited[0] = 1
    cnt = 0
    primenumberlist = [s for s in numbers]
    for i in range(1,len(numbers)+1):
        use = list(permutations(primenumberlist, i))
        for case in use:
            if isPrime(int("".join(case)),visited):
                cnt += 1
    return cnt
print(solution("011"))