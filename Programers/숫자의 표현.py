def solution(n):
    i = 2  # 붙어있는 자연수의 갯수
    ret = 0
    while True:
        n_sum = 0
        for cnt in range(1, i):
            n_sum += cnt
        if n_sum > n:  # end
            break
        while n_sum < n:
            n_sum += (i - 1)
        if n_sum == n:
            ret += 1
        i += 1
    return ret


print(solution(15))
