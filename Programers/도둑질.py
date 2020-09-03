def solution(money):
    dp = [0 for _ in range(len(money))]  # i번을 범위에 넣었을 때, 0~i까지의 최댓값
    dp_no_house_zero = [0 for _ in range(len(money))]  # i번을 범위에 넣었을 때, 1~i까지의 최댓값
    # init
    dp[0], dp[1] = money[0], max(money[0], money[1])
    dp_no_house_zero[0] = 0
    dp_no_house_zero[1] = money[1]

    for i in range(2, len(money) - 1):
        dp[i] = max(money[i] + dp[i - 2], dp[i - 1])
        dp_no_house_zero[i] = max(money[i] + dp_no_house_zero[i - 2], dp_no_house_zero[i - 1])
    i += 1
    return max(money[i] + dp_no_house_zero[i - 2], dp[i - 1])