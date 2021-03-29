def solution(strs, t):
    dp = [len(t)+1 for _ in range(len(t))]
    for _ in range(5):
        dp.append(0)

    for i in range(len(t)-1, -1, -1):
        for k in range(1,6):
            if t[i:i+k] in strs:
                val1 = dp[i]
                val2 = dp[i+k]+1
                dp[i] = min(val1, val2)
    return dp[0] if dp[0] != len(t)+1 else -1

print(solution(['ba','na','n','a'],"banana"))
