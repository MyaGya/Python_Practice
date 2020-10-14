def solution(n):
    dp = [0 for _ in range(n+1)] # 괄호쌍 dp[x] 개로 만들 수 있는 수
    dp[0] = 1
    dp[1] = 1

    for i in range(2,n+1):
        for j in range(1,i+1):
            dp[i] += dp[j-1] * dp[i-j]
    return dp[n]


print(solution(14))