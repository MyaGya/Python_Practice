def solution(n, a, b):
    if a > b:
        a, b = b, a
    answer = 1
    while not (a + 1 == b and a % 2 == 1 and b % 2 == 0):
        if a % 2 == 0:
            a //= 2
        else:
            a = a // 2 + 1

        if b % 2 == 0:
            b //= 2
        else:
            b = b // 2 + 1
        answer += 1

    return answer
