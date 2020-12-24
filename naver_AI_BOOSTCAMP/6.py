from collections import deque


def solution(nums=[4, 1, 2, 3, 1, 0, 5]):
    visited = {}
    stack = deque()
    stack.append([0, 0])

    while (stack):
        pos, depth = stack.popleft()
        if pos == len(nums) - 1:
            return depth

        if 0 < pos - nums[pos]:
            stack.append([pos - nums[pos], depth + 1])
        if pos + nums[pos] < len(nums):
            stack.append([pos + nums[pos], depth + 1])