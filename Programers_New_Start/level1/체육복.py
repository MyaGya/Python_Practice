from collections import defaultdict


def solution(n, lost, reserve):
    ans = 0
    students_uniform = defaultdict(lambda: 1)

    for i in reserve:
        students_uniform[i] += 1
    for i in lost:
        students_uniform[i] -= 1

    for i in lost:
        if students_uniform[i] == 1:  # 도난당하고 2개 가져온 경우
            ans += 1
            continue
        if students_uniform[i - 1] == 2:  # 앞에 사람에게 빌리는 경우
            students_uniform[i - 1] = 1
            ans += 1
        elif students_uniform[i + 1] == 2:  # 뒤에 사람에게 빌리는 경우
            students_uniform[i + 1] = 1
            ans += 1

    return ans + (n - len(lost))


print(solution(5, [2, 4], [1, 3, 5]))
