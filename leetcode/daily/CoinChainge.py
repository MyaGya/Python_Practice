from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount // coins[0] + 1]


solution = Solution()
print(solution.coinChange([2], 3))
