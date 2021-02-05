def solution(n, money):
    dp = [0 for _ in range(n + 1)]
    money.sort()

    for i in range(0, n+1, money[0]):  # 0 일 때에는 조건을 충조시켰으니 1
        dp[i] = 1

    for now_money in money[1:]:
        for i in range(now_money, n + 1):
            dp[i] += dp[i - now_money] % 1000000007
    return dp[n]


print(solution(5, [1, 2, 5]))
