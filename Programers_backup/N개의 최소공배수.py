import math


def solution(arr):
    if len(arr) == 1:
        return arr[0]
    value1 = arr[0]
    multiply = arr[0]
    for value2 in arr[1:]:
        value1 = math.gcd(value1, value2)
        multiply = multiply * value2 // value1
    return multiply

print(solution([2,6,8,14]))