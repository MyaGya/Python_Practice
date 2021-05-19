def solution(numbers):
    answer = []
    for number in numbers:
        binary_value = list(reversed(bin(number)[2:]))
        if binary_value.count('0') == 0:
            binary_value[-1] = '0'
            binary_value.append('1')
        else:
            for i in range(len(binary_value)):
                if binary_value[i] == '0':
                    if i != 0:
                        binary_value[i] = '1'
                        binary_value[i - 1] = '0'
                    elif i == 0:
                        binary_value[i] = '1'
                    break

        answer.append(int("".join(reversed(binary_value)), 2))
    return answer


print(solution([11, 100, 127, 128, 129, 130, 140, 143]))
