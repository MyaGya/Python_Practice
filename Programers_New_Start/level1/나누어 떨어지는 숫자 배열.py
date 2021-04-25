def solution(arr, divisor):
    return sorted([value for value in arr if value % divisor == 0]) or [-1]
