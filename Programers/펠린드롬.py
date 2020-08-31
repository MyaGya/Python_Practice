def solution(s):
    dp = [[False for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
    max_jump = 0
    for jump in range(2,len(s)):
        for i in range(len(s)-jump):
            after_jump = i + jump
            if s[i] == s[after_jump] and dp[i+1][after_jump-1]:
                dp[i][after_jump] = True
                max_jump = max(max_jump,jump)
    return max_jump + 1


print(solution('abba'))