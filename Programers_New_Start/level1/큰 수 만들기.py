def solution(number, k):
    answer = []
    index = 0
    while k and index != len(number):
        if not answer or answer[-1] >= number[index]:
            answer.append(number[index])
            index += 1
        else:
            answer.pop()
            k -= 1

    if k == 0:
        return "".join(answer) + number[index:]
    else:
        return number[:len(number) - k]


print(solution("1924", 2))
