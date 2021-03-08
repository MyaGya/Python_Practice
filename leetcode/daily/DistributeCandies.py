from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        max_candies = len(candyType) // 2
        type_of_candy = len(set(candyType))
        return max_candies if max_candies < type_of_candy else type_of_candy


solution = Solution()
print(solution.distributeCandies([1, 1, 2, 2, 3, 3]))
