def solution(n):
    make_n = []
    while n:
        make_n.append(n % 3)
        n //= 3

    multiplier = 0
    ret = 0
    for i in reversed(make_n):
        ret += i * (3 **multiplier)
        multiplier += 1
    return ret


print(solution(125))