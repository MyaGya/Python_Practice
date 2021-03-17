'''
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
'''


def solution(progresses, speeds):
    i = 0
    need_day = [(100 - progresses[i]) // speeds[i] if (100 - progresses[i]) % speeds[i] == 0
                else (100 - progresses[i]) // speeds[i] + 1
                for i in range(len(progresses))]
    ans = []
    while i < (len(progresses)):
        total = 0
        standard = need_day[i]
        while i < len(progresses) and need_day[i] <= standard :
            total += 1
            i += 1
        ans.append(total)
    return ans

print(solution([93,30,55], [1,30,5]))
