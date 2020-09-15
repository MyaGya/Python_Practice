def solution(n):
    number = 1
    front = [[] for _ in range(n + 1)]
    back = [[] for _ in range(n + 1)]

    value, remain = divmod(n, 3)

    if remain != 0:
        value += 1

    start = 1
    end = n
    number = 1
    while start <= end:
        for i in range(start, end):  # 밑으로 쭉 내려가는 연산
            front[i].append(number)
            number += 1
        for i in range(end - (len(front[end]) + len(back[end]) + 1)):  # 오른쪽으로 채우는 연산
            front[end].append(number)
            number += 1
        for i in range(end, start, -1):  # 위로 올라가는 연산
            back[i].append(number)
            number += 1
        if start == end:
            front[start].append(number)
        start += 2
        end -= 1
    ret = []

    for i in range(1, n + 1):
        back[i].reverse()
        ret += front[i] + back[i]
    return ret
print(solution(5))