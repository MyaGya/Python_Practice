def solution(progresses, speeds):
    day = 0
    ans = []
    same_time = 0
    for progress, speed in zip(progresses, speeds):
        complete_day, remain = divmod(100 - progress, speed)
        complete_day = complete_day if remain == 0 else complete_day + 1

        if day < complete_day:
            day = complete_day
            ans.append(same_time)
            same_time = 1
        else:
            same_time += 1
    else:
        ans.append(same_time)

    return ans[1:]
