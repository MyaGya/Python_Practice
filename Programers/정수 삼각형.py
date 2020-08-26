def solution(triangle):
    dp = [triangle[0]]
    dp[0] = triangle[0]
    for Lst in range(1, len(triangle)):
        tmp = [0] * len(triangle[Lst]) # 최대 배열(dp에 편입)
        for i in range(len(triangle[Lst])-1): # 이전 dp배열을 기준으로 값 삽입
            tmp[i] = max(dp[Lst-1][i] + triangle[Lst][i],tmp[i]) # 값이 2번 들어가야 하므로 비교연산 진행
            tmp[i+1] = dp[Lst-1][i] + triangle[Lst][i+1] #
        dp.append(tmp)
    return max(dp[len(triangle)-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))