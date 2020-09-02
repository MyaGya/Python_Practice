def solution(arr, divisor):
    ret = [i for i in sorted(arr) if i%divisor == 0]
    if not ret:
        return -1
    return ret

print(solution([5, 9, 7, 10],5))