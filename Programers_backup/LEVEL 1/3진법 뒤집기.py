def solution(n):
    change = ""
    # 3진법 변경
    while n:
        change =str(n % 3) + change
        n = n // 3
    ret = 0
    for i in range(len(change)):
        ret += int(change[i]) * (3 ** i)
    return ret

print(solution(45))