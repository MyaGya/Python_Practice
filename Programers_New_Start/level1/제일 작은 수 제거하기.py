def solution(arr):
    ans = []
    min_arr = min(arr)
    for value in arr:
        if value == min_arr:
            continue
        ans.append(value)
    return ans if ans else [-1]
