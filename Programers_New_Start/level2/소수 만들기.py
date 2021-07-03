import math


def solution(nums):
    max_n = 3000
    # make prime number
    prime_number = [True for _ in range(max_n)]
    for i in range(2, int(math.sqrt(max_n)) + 1):
        j = 2
        while (i * j < max_n):
            prime_number[i * j] = False
            j += 1

    answer = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if prime_number[nums[i] + nums[j] + nums[k]]:
                    answer += 1
    return answer


print(solution([1, 2, 7, 6, 4]))
