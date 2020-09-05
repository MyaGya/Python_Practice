def solution(arr):
    ans = [arr[0]]
    cur = arr[0]
    for i in arr[1:]:
        if i != cur:
            ans.append(i)
            cur = i
    print(arr[::-1])
    return ans

print(solution([1,1,3,3,0,1,1]	))