def solution(msg):
    # init
    data = dict()
    prepare = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(27):
        data[prepare[i-1]] = i

    answer = []
    # solution
    i = 0
    tmp = ""
    order = 27
    while i < len(msg):
        tmp += msg[i]
        i += 1
        # find fail
        if data.get(tmp) == None:
            data[tmp] = order
            order += 1
            answer.append(data[tmp[:-1]])
            tmp = ""
            i -= 1
        elif i == len(msg):
            answer.append(data[tmp])

    return answer


print(solution(input()))