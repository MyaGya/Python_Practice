def solution(N, number):
    data = [[0]]

    for i in range(1, 9):
        data.append([int(str(N) * i)])
        new_data = []
        for mid in range(0, i):
            for before_value in data[i - mid]:
                for after_value in data[mid]:
                    new_data.append(before_value + after_value)  # 덧셈
                    new_data.append(before_value - after_value)  # 뺄셈
                    new_data.append(before_value * after_value)  # 곱셈
                    if after_value != 0:
                        new_data.append(before_value // after_value) # 나눗셈
            if number in new_data:
                return i
            data.pop()
            data.append(list(set(new_data)))
    return -1

print(solution(4,17))