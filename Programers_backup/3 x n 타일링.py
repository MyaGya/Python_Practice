def solution(n):
    divisor = 1000000007
    data = [1] * (n+1)
    data[2] = 3
    etc = 0
    for i in range(4, n+1, 2):
        etc += data[i - 4] * 2 % divisor
        data[i] = (data[i-2] * 3 + etc) % divisor
    return data[n]

print(solution(4))