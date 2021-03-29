def solution(n, times):
    L = 0
    R = n * times[0]
    while L <= R:
        mid = (L + R) // 2
        enable = 0
        for time in times:
            enable += mid // time
        if enable < n:
            L = mid + 1
        else:
            R = mid - 1
            ret = mid
    return ret
print(solution(6,[7,10]))