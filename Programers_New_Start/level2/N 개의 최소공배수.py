import math

def solution(arr):
    answer = 1
    for value in arr:
        answer *= value // math.gcd(answer, value)

    return answer


print(solution([2, 6, 8, 14]))
