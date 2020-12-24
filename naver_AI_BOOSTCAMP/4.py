def solution(n):
    data = {}

    for i in range(1, 1000000):
        value = i
        for j in range(i + 1, 1000000):
            value *= j
            data[value] = True
            if value > 10 ** 12:
                break

    print("test")
    answer_list = sorted(data.keys())

    print(answer_list[n-1])




print(solution(2))
