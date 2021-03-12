# 4 7
# 6 13
# 4 8
# 3 6
# 5 12
n, k = map(int, input().split())
data = []

dp = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]
data.sort(key=lambda x: x[0])

data.append([0, 0])
for _ in range(n):
    data.append(list(map(int, input().split())))

i = 0
for weight, value in data:
    if weight < n - 1:
        dp[i][weight] = value
    i += 1


def value_of_dp(col, row):
    if col < 0 or row < 0:  # 잘못된 값이라면
        return 0
    if dp[col][row] != -1:  # 값이 설정되어 있다면
        return dp[col][row]

    value1 = value_of_dp(col - 1, row)
    value2 = value_of_dp(col - 1, row - data[col][0]) + data[col][1] if row - data[col][0] >= 0 else 0
    dp[col][row] = max(value1, value2)
    return dp[col][row]


print(value_of_dp(n, k))
