cnt = 0
def dfs(numbers, target, valueSum, i):
    global cnt
    if i == len(numbers):
        if valueSum == target:
            cnt += 1
        return
    dfs(numbers, target, valueSum + numbers[i], i + 1)
    dfs(numbers, target, valueSum - numbers[i], i + 1)

def solution(numbers, target):
    dfs(numbers,target,0,0)
    return cnt


print(solution([1, 1, 1], 3))
