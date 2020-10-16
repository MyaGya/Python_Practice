def check(arr, x1, x2, y1, y2):
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            if arr[y1][x1] != arr[i][j]:
                return False
    return True


def divide(arr, x1, x2, y1, y2, ret: list):
    if check(arr, x1, x2, y1, y2):  # end
        if arr[y1][x1] == 0:
            ret[0] += 1
        else:
            ret[1] += 1
        return
    mid = (x2 - x1 + 1) // 2 - 1 # 몇 칸인지에 대한 정보
    divide(arr, x1, x1 + mid, y1, y1 + mid, ret)
    divide(arr, x1 + mid + 1, x2, y1, y1 + mid, ret)
    divide(arr, x1, x1 + mid, y1 + mid + 1, y2, ret)
    divide(arr, x1 + mid + 1, x2, y1 + mid + 1, y2, ret)


def solution(arr):
    ret = [0, 0]
    divide(arr, 0, len(arr) - 1, 0, len(arr) - 1, ret)
    return ret


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
