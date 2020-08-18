def solution(progresses, speeds):
    answer = []
    lazy = 0
    cnt = 0
    for i in range(len(progresses)):
        if  progresses[i] + lazy * speeds[i] < 100:
            answer.append(cnt)
            cnt = 1
            lazy = (100 - progresses[i]) // speeds[i]
            if (100 - progresses[i]) % speeds[i]:
                lazy += 1
        else:
            cnt += 1
    answer.append(cnt)
    return answer[1:]

print(solution([93,30,55], [1,30,5]))
