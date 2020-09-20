def solution(n, works):
    works.sort(reverse=True)

    while n and works[-1] != 0:

        if works[0] == works[-1]: # works의 수가 모두 동일할 경우 평탄화작업만 진행한다
            for i in range(len(works)):
                works[i] -= 1
                n -= 1
                if n == 0:
                    break
            continue

        for i in range(1, len(works)):
            if works[i - 1] > works[i]:
                break

        if (i + 1) * (works[i - 1] - works[i]) <= n:  # 다 일을 할 수 있을 경우
            for j in range(i - 1, -1, -1):
                n -= works[j] - works[i]
                works[j] = works[i]
        else:  # 다 일을 할 수 없을 경우
            while n:  # n을 쓰면서 하나씩 줄여나간다
                for j in range(i):
                    n -= 1
                    works[j] -= 1
                    if n == 0:
                        break

    return sum([value ** 2 for value in works])

print(solution(3,[1,1]))