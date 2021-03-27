def solution(n):
    base3 = ""
    while n:
        base3 = str(n % 3) + base3
        n = n // 3

    ans = 0
    for i in range(len(base3)):
        ans += int(base3[i]) * (3 ** i)

    return ans


print(solution(45))
