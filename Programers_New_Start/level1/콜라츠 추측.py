def solution(num):
    ans = 0

    while (num != 1 and ans != 500):
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        ans += 1
    return ans if ans != 500 else -1
