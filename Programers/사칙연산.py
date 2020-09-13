def solution(arr):
    mx = [[None for i in range(len(arr))] for j in range(len(arr))]
    mi = [[None for i in range(len(arr))] for j in range(len(arr))]

    def calcMx(L, R):  # MAX를 찾는 dp
        if L == R:
            mx[L][R] = int(arr[L])
            mi[L][R] = int(arr[L])
        if mx[L][R]:
            return mx[L][R]

        waiting_sum = []
        for i in range(L + 1, R, 2):  #
            if arr[i] == '+':  # +일경우
                waiting_sum.append(calcMx(L,i - 1) + calcMx(i + 1,R))
            else:
                waiting_sum.append(calcMx(L,i - 1) - calcMi(i + 1,R))
        mx[L][R] = max(waiting_sum)
        return mx[L][R]

    def calcMi(L, R):  # MIN를 찾는 dp
        if L == R:
            mx[L][R] = int(arr[L])
            mi[L][R] = int(arr[L])
        if mi[L][R]:
            return mi[L][R]
        waiting_sum = []
        for i in range(L + 1, R, 2):  #
            if arr[i] == '+':  # +일경우
                waiting_sum.append(calcMi(L,i - 1) + calcMi(i + 1,R))
            else:
                waiting_sum.append(calcMi(L,i - 1) - calcMx(i + 1,R))
        mi[L][R] = min(waiting_sum)
        return mi[L][R]
    # 1. run
    return calcMx(0, len(arr)-1)


print(solution(['5', '-', '3', '+', '1', '+', '2', '-', '4']))


