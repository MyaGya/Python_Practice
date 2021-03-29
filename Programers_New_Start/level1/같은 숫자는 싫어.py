def solution(arr):
    ans = []
    ans.append(arr[0])
    for value in arr:
        if ans[-1] == value:
            continue

        ans.append(value)
    return ans


print(solution([1, 1, 3, 3, 0, 1, 1]))
