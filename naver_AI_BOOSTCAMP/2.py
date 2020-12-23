def solution(arr):
    ans = 0
    while(len(arr) != 1):
        ans += 1
        new_arr = []
        duplicate = 1;
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                duplicate += 1
            else:
                new_arr.append(duplicate)
                duplicate = 1
        else:
            new_arr.append(duplicate)
        print(new_arr)
        arr = new_arr
    return ans
print(solution([1, 1, 3, 3, 2, 2, 4, 5, 1, 1, 1, 3]))
