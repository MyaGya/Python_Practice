def solution(nums):
    num_pocketmon = len(nums) // 2

    return min(len(set(nums)), num_pocketmon)
